import pandas as pd

# We create a function to calculate the weight of the harassment
# with different types of calculation, to make an analysis of the results depending on the type of weight
def weight_harassment_calculation(length, harassment_risk, type_weight):
    # Calculate the weight of the harassment
    if type_weight == 1:
        return length*30 + harassment_risk*500
    elif type_weight == 2:
        return length * harassment_risk
    else:
        return length**(harassment_risk*10)


def create_graph(type_weight):
    # Read the data with Pandas
    df = pd.read_csv('./data/calles_de_medellin_con_acoso.csv', sep=";")
    # Fill N.A values in the data with the mean of the harassmentRisk column
    df.harassmentRisk.fillna(df.harassmentRisk.mean(), inplace=True)
    # Create a graph
    graph = {}

    # Iterate over the data with the itertuples method
    # That creates a tuple with the values of each row
    for row in df.itertuples():
        # Get the data from the row in each column
        # The first column is the name, so we start from the second

        # The origin of the street, will save in another tuple and convert to float
        origin = row[2][1:-1].split(", ")
        origin = (float(origin[0]), float(origin[1]))
        # The destination of the street, will save in another tuple and convert to float
        destination = row[3][1:-1].split(", ")
        destination = (float(destination[0]), float(destination[1]))
        # The risk of harassment in the street calculated with the length and the harassmentRisk coefficient
        # The weight calculated depending on the type of weight chosen
        if type_weight == 1:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), type_weight)
        elif type_weight == 2:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), type_weight)
        else:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), 3)
        length = float(row[4])
        name = row[1]
        # Add the origin to the graph as a key, verifying if it is not already in the graph
        # If it is not in the graph, add it with an empty dictionary
        if origin not in graph:
            graph[origin] = {}

        # Add the destination of the origin to the graph as a key of the origin dictionary
        # Add it with the weight of the harassment and the length of the street
        graph[origin][destination] = weight_harassment, length, name

        # Check if the origin is oneway or not
        # If it is it, add the destination as an origin and the origin as a destination with the same weight and length
        if row[5] is True:
            if destination not in graph:
                graph[destination] = {}
            graph[destination][origin] = weight_harassment, length, name
    return graph
