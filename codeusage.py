import streamlit as st
import time
import psutil
import plotly.express as px
import pandas as pd
import threading




# Function to execute code and collect performance metrics
def execute_code(code, cpu_data, memory_data, time_data, interval=1):
    process = psutil.Process()
    start_time = time.time()

    # Execute the code once
    exec(code)

    # Collect performance metrics over time
    while time.time() - start_time < 10:  # Run for 10 seconds
        cpu_usage = psutil.cpu_percent(interval=interval)
        memory_usage = process.memory_info().rss / (1024 * 1024)  # in MB
        elapsed_time = time.time() - start_time

        # Append data to lists
        time_data.append(elapsed_time)
        cpu_data.append(cpu_usage)
        memory_data.append(memory_usage)

        # Sleep for the specified interval
        time.sleep(interval)

# Button to execute both codes in parallel
def visualisation(optimized_code,unoptimized_code):
    try:
        # Lists to store performance data for optimized and unoptimized code
        optimized_cpu_data = []
        optimized_memory_data = []
        optimized_time_data = []

        unoptimized_cpu_data = []
        unoptimized_memory_data = []
        unoptimized_time_data = []

        # Placeholder for dynamic graph updates
        cpu_placeholder = st.empty()
        memory_placeholder = st.empty()

        # Create threads to run both codes in parallel
        optimized_thread = threading.Thread(
            target=execute_code,
            args=(optimized_code, optimized_cpu_data, optimized_memory_data, optimized_time_data)
        )
        unoptimized_thread = threading.Thread(
            target=execute_code,
            args=(unoptimized_code, unoptimized_cpu_data, unoptimized_memory_data, unoptimized_time_data)
        )

        # Start the threads
        optimized_thread.start()
        unoptimized_thread.start()

        # Counter to generate unique keys for each update
        update_counter = 0

        # Update graphs in real-time
        while optimized_thread.is_alive() or unoptimized_thread.is_alive():
            # Create a DataFrame for plotting
            df = pd.DataFrame({
                "Time (s)": optimized_time_data + unoptimized_time_data,
                "CPU Usage (%)": optimized_cpu_data + unoptimized_cpu_data,
                "Memory Usage (MB)": optimized_memory_data + unoptimized_memory_data,
                "Code Type": ["Optimized"] * len(optimized_time_data) + ["Unoptimized"] * len(unoptimized_time_data)
            })

            # Update CPU usage graph
            fig_cpu = px.line(df, x="Time (s)", y="CPU Usage (%)", color="Code Type",
                              title="CPU Usage Over Time (Optimized vs Unoptimized)")
            cpu_placeholder.plotly_chart(fig_cpu, key=f"cpu_plot_{update_counter}")  # Unique key for CPU plot

            # Update memory usage graph
            fig_memory = px.line(df, x="Time (s)", y="Memory Usage (MB)", color="Code Type",
                                 title="Memory Usage Over Time (Optimized vs Unoptimized)")
            memory_placeholder.plotly_chart(fig_memory, key=f"memory_plot_{update_counter}")  # Unique key for memory plot

            # Increment the counter for the next update
            update_counter += 1

            # Sleep for a short interval to avoid excessive updates
            time.sleep(1)

        # Wait for threads to finish
        optimized_thread.join()
        unoptimized_thread.join()

        # Display success message
        st.success("Codes executed successfully!")

    except Exception as e:
        st.error(f"Error executing code: {e}")