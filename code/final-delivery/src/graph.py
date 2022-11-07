import pandas as pd


def weight_harassment_calculation(length, harassment_risk, type_weight):
    if type_weight == 1:
        return length*30 + harassment_risk*500
    elif type_weight == 2:
        return length * harassment_risk
    else:
        return length**(harassment_risk*10)


def create_graph(type_weight):
    df = pd.read_csv('./data/calles_de_medellin_con_acoso.csv', sep=";")
    df.harassmentRisk.fillna(df.harassmentRisk.mean(), inplace=True)
    graph = {}

    for row in df.itertuples():
        origin = row[2][1:-1].split(", ")
        origin = (float(origin[0]), float(origin[1]))

        destination = row[3][1:-1].split(", ")
        destination = (float(destination[0]), float(destination[1]))

        if type_weight == 1:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), type_weight)
        elif type_weight == 2:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), type_weight)
        else:
            weight_harassment = weight_harassment_calculation(float(row[4]), float(row[6]), type_weight)

        length = float(row[4])
        name = row[1]
        harassment = float(row[6])

        if origin not in graph:
            graph[origin] = {}

        graph[origin][destination] = weight_harassment, length, name, harassment

        if row[5] is True:
            if destination not in graph:
                graph[destination] = {}
            graph[destination][origin] = weight_harassment, length, name, harassment

    return graph
