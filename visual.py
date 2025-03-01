import streamlit as st
import ast
import json
import streamlit.components.v1 as components

# Function to extract nodes and edges from AST
def parse_ast(code):
    tree = ast.parse(code)
    nodes = []
    edges = []
    node_id = 0

    def add_node(name, parent=None, node_type="default"):
        """Creates a new node and adds it to the graph."""
        nonlocal node_id
        node = {"data": {"id": str(node_id), "label": name, "type": node_type}}
        nodes.append(node)
        if parent is not None:
            edges.append({"data": {"source": str(parent), "target": str(node_id)}})
        node_id += 1
        return node_id - 1

    start_id = add_node("Start", node_type="start")
    parent_stack = [start_id]
    last_nodes = []  # Track last nodes to connect to the End node

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            parent_id = add_node(f"Function: {node.name}", parent_stack[-1], "function")
            parent_stack.append(parent_id)
            last_nodes.append(parent_id)

        elif isinstance(node, ast.If):
            condition_text = ast.unparse(node.test) if hasattr(ast, "unparse") else "Condition"
            cond_id = add_node(f"If: {condition_text}", parent_stack[-1], "condition")

            true_branch = add_node("True", cond_id, "branch")
            false_branch = add_node("False", cond_id, "branch")

            parent_stack.append(true_branch)
            last_nodes.append(false_branch)

        elif isinstance(node, (ast.For, ast.While)):
            loop_id = add_node("Loop", parent_stack[-1], "loop")
            edges.append({"data": {"source": str(loop_id), "target": str(loop_id)}})  # Self-loop
            parent_stack.append(loop_id)
            last_nodes.append(loop_id)

    end_id = add_node("End", node_type="end")
    for node in last_nodes:
        edges.append({"data": {"source": str(node), "target": str(end_id)}})

    return nodes, edges

# Streamlit UI
def streamlit_ui(code):
        if code.strip():
            nodes, edges = parse_ast(code)

            # Convert to JSON format for Cytoscape.js
            graph_data = json.dumps({"nodes": nodes, "edges": edges})

            # Cytoscape.js visualization with full-screen mode
            html_code = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.21.1/cytoscape.min.js"></script>
                <style>
                    body, html {{
                        margin: 0;
                        padding: 0;
                        overflow: hidden;
                    }}
                    #cy {{
                        width: 100%;
                        height: 500px;
                        border: 1px solid #ddd;
                        transition: all 0.3s ease-in-out;
                    }}
                    #cy.fullscreen {{
                        width: 100vw;
                        height: 100vh;
                        position: fixed;
                        top: 0;
                        left: 0;
                        background: white;
                        z-index: 9999;
                    }}
                </style>
            </head>
            <body>
                <div id="cy"></div>
                <script>
                    var cy = cytoscape({{
                        container: document.getElementById('cy'),
                        elements: {graph_data},
                        style: [
                            {{ selector: 'node', style: {{
                                'background-color': '#0074D9',
                                'label': 'data(label)',
                                'color': 'white',
                                'text-valign': 'center',
                                'text-halign': 'center',
                                'font-size': '12px',
                                'opacity': 0  // Initially hidden for animation
                            }} }},
                            {{ selector: 'node[type="start"]', style: {{
                                'background-color': '#2ECC40',
                                'shape': 'round-rectangle'
                            }} }},
                            {{ selector: 'node[type="end"]', style: {{
                                'background-color': '#FF4136',
                                'shape': 'round-rectangle'
                            }} }},
                            {{ selector: 'node[type="condition"]', style: {{
                                'background-color': '#FFDC00',
                                'shape': 'diamond'
                            }} }},
                            {{ selector: 'node[type="loop"]', style: {{
                                'background-color': '#FF851B',
                                'shape': 'ellipse'
                            }} }},
                            {{ selector: 'node[type="function"]', style: {{
                                'background-color': '#B10DC9',
                                'shape': 'round-rectangle'
                            }} }},
                            {{ selector: 'edge', style: {{
                                'width': 2,
                                'line-color': '#AAB7B8',
                                'target-arrow-shape': 'triangle',
                                'curve-style': 'bezier',
                                'opacity': 0  // Initially hidden for animation
                            }} }}
                        ],
                        layout: {{
                            name: 'breadthfirst',
                            directed: true,
                            padding: 10
                        }}
                    }});

                    // Animation to fade in nodes
                    cy.nodes().forEach((node, i) => {{
                        setTimeout(() => {{
                            node.animate({{
                                style: {{ opacity: 1 }},
                                duration: 500
                            }});
                        }}, i * 200);
                    }});

                    // Animation to fade in edges after nodes
                    setTimeout(() => {{
                        cy.edges().forEach((edge, i) => {{
                            setTimeout(() => {{
                                edge.animate({{
                                    style: {{ opacity: 1 }},
                                    duration: 300
                                }});
                            }}, i * 150);
                        }});
                    }}, 1000);

                    // Traversal Animation on Node Click
                    cy.on('tap', 'node', function(evt) {{
                        var node = evt.target;

                        // Reset all nodes and edges to default color
                        cy.nodes().style({{ 'background-color': '#0074D9' }});
                        cy.edges().style({{ 'line-color': '#AAB7B8' }});

                        // Highlight clicked node and its outgoing edges
                        node.style('background-color', '#FF4136');
                        var outgoingEdges = node.outgoers('edge');
                        outgoingEdges.style('line-color', '#FF4136');

                        // Traverse path dynamically
                        var targetNodes = outgoingEdges.targets();
                        let delay = 500;
                        targetNodes.forEach((target, index) => {{
                            setTimeout(() => {{
                                target.style('background-color', '#FFDC00');  // Highlight next node
                            }}, delay * (index + 1));
                        }});
                    }});

                    // Full-screen toggle on click
                    document.getElementById('cy').addEventListener('click', function() {{
                        this.classList.toggle('fullscreen');
                    }});
                </script>
            </body>
            </html>
            """

            components.html(html_code, height=550)
            return graph_data  # Return visualization data
        else:
            st.error("Please enter valid Python code!")
            return None