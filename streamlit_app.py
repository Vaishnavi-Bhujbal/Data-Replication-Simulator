
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Replication Simulator", layout="wide")

st.title("💾 Data Replication Simulator")
st.write("A web-based simulation of distributed data replication.")

# Initialize nodes
if "nodes" not in st.session_state:
    st.session_state.nodes = {
        "Node 1": {"status": "Active", "data": []},
        "Node 2": {"status": "Active", "data": []},
        "Node 3": {"status": "Active", "data": []}
    }

st.subheader("Distributed Nodes")

cols = st.columns(3)

for i, (node, details) in enumerate(st.session_state.nodes.items()):
    with cols[i]:
        st.metric(node, details["status"])
        st.write("Stored Records:", len(details["data"]))

st.divider()

st.subheader("Insert New Data")

record = st.text_input("Enter data to store")

if st.button("Insert and Replicate"):
    if record.strip():
        st.session_state.nodes["Node 1"]["data"].append(record)

        for node in ["Node 2", "Node 3"]:
            if st.session_state.nodes[node]["status"] == "Active":
                st.session_state.nodes[node]["data"].append(record)

        st.success("Data inserted and replicated successfully!")
    else:
        st.warning("Please enter some data.")

st.divider()

st.subheader("Node Failure Simulation")

selected_node = st.selectbox(
    "Select a node",
    list(st.session_state.nodes.keys())
)

if st.button("Simulate Node Failure"):
    st.session_state.nodes[selected_node]["status"] = "Failed"
    st.warning(selected_node + " has failed!")

if st.button("Recover Node"):
    st.session_state.nodes[selected_node]["status"] = "Active"
    st.session_state.nodes[selected_node]["data"] = list(
        st.session_state.nodes["Node 1"]["data"]
    )
    st.success(selected_node + " recovered successfully!")

st.divider()

st.subheader("Stored Data")

for node, details in st.session_state.nodes.items():
    st.write("**" + node + "**")
    st.write(details["data"])
