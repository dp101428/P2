
def find_path (source_point, destination_point, mesh):

    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

#identify the source and Destination boxes
	#scan through boxes to find which contains the source point

	boxes = mesh["boxes"]



	for element in boxes:
		if((source_point[0] >= element[0]) and (source_point[0] <= element[1]) and (source_point[1] <= element[2]) and (source_point[1] >= element[3])):
			startingBox = (element)
			print("Starting Box found at: " + element)
		if((destination_point[0] >= element[0] and (destination_point[0] <= element[1]) and (destination_point[1] <= element[2]) and (destination_point[1] >= element[3])):
			goalBox = (element)
			print("Goal Box found at: " + element)

	

	#scan through boxes to find the destination point

	#return a list of the 2 boxes with the source and destination






#Modify your Dijkstra's search to compute a legal list of line segments demonstrating the path
    #set up data structures for search
#Convert Dijkstra's into A*

#Modify your A* into a Bidirectional A*


    path = []
    boxes = {}

    return path, boxes.keys()
