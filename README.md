# graph-algorithm

This is my solution to a graph theory problem formulated as part of the Algorithmic Thinking course, organised by Rice University's Department of Computer Science.

Here, I compute the in-degree distribution of random directed graphs generated by my implementation of algorithm ER, and directed graphs generated by my implementation of algorithm DPA. I compare this to the in-degree distribution of a collection of 27,770 high energy physics theory papers represented as a graph, where the "paper i cites paper j" relationship is represented by an directed edge from node i to node j. We find that the citation graph's in-degree distribution resembles that of the DPA graph, indicating that the "rich gets richer" phenomenon is at work in citations.

Due to the highly specific nature of the modules imported, it only works in CodeSkulptor - you can access it at https://py2.codeskulptor.org/#user48_ajWw9tjO2A_37.py
