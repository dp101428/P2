from heapq import heappop, heappush
import math
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
    path = []
    boxes = {}
#identify the source and Destination boxes
	#scan through boxes to find which contains the source point

    box = mesh["boxes"]

    print(mesh)

    for element in box:
        print(element)
        if((source_point[0] >= element[0]) and (source_point[0] <= element[1]) and (source_point[1] >= element[2]) and (source_point[1] <= element[3])):
            startingBox = (element)
            print("Starting Box found at: ")
            print(element)
        if((destination_point[0] >= element[0]) and (destination_point[0] <= element[1]) and (destination_point[1] >= element[2]) and (destination_point[1] <= element[3])):
            goalBox = (element)
            print("Goal Box found at: ")
            print(element)



	#scan through boxes to find the destination point

	#return a list of the 2 boxes with the source and destination






#Modify your Dijkstra's search to compute a legal list of line segments demonstrating the path
    #set up data structures for search
    #First we're just doing a basic BFS
    toSearch = [(0,startingBox, "dest")]
    heappush(toSearch, (0, goalBox, "start"))
    
    cameFromFront = {startingBox : None}
    costToFront = {startingBox : 0}
    cameFromBack = {goalBox : None}
    costToBack = {goalBox : 0}
    #Adding a record of the point location within the box
    boxes[startingBox] = source_point
    boxes[goalBox] = destination_point
    #While there's things to search
    while toSearch:
        #Get the next thing to check
        nextNodeCost, nextNode, goal = heappop(toSearch)

        #Find the heuristic from this point to the end
        if(goal == "dest"):
            estToEnd = math.sqrt((destination_point[0] -boxes[nextNode][0]) * (destination_point[0] -boxes[nextNode][0]) + (destination_point[1] -boxes[nextNode][1]) * (destination_point[1] -boxes[nextNode][1]))
        else:
            estToEnd = math.sqrt((source_point[0] -boxes[nextNode][0]) * (source_point[0] -boxes[nextNode][0]) + (source_point[1] -boxes[nextNode][1]) * (source_point[1] -boxes[nextNode][1]))
        #See if it's the goal
        """
        if nextNode == goalBox:
            #Do this later
            path.append(boxes[nextNode])
            path.append(destination_point)
            priorNode = cameFrom[nextNode]
            while priorNode is not None:
                path.insert(0, boxes[priorNode])
                priorNode = cameFrom[priorNode]
            break
        """
        
        #Otherwise, keep finding things to put in the queue
        for box in mesh["adj"][nextNode]:
            pathToNew = shortest_path_to_box(boxes[nextNode], nextNode, box)
            lengthOfPath = math.sqrt(pathToNew[0] * pathToNew[0] + pathToNew[1] * pathToNew[1])
            if (goal == "dest"):
                if(box in costToBack):
                    #Do this later
                    path.append(boxes[nextNode])
                    priorNode = cameFromBack[box]
                    while priorNode is not None:
                        path.append(boxes[priorNode])
                        priorNode = cameFromBack[priorNode]
                    path.append(destination_point)
                    priorNode = cameFromFront[nextNode]
                    while priorNode is not None:
                        path.insert(0,boxes[priorNode])
                        priorNode = cameFromFront[priorNode]
                    path.insert(source_point)
                    return resolvePathfinding(path, boxes)
                estToEnd = math.sqrt((destination_point[0] -pathToNew[0]) * (destination_point[0] -pathToNew[0]) + (destination_point[1] -pathToNew[1]) * (destination_point[1] -pathToNew[1]))
                totalCostTo = costToFront[nextNode] + lengthOfPath
                if(box not in cameFromFront or costToFront[box] > totalCostTo +  + estToEnd):
                    heappush(toSearch, (totalCostTo  + estToEnd, box))
                    cameFromFront[box] = nextNode
                    boxes[box] = pathToNew
                    costToFront[box] = totalCostTo
            else:
                if(box in costToFront):
                    #Do this later
                    path.append(boxes[nextNode])
                    priorNode = cameFromBack[nextNode]
                    while priorNode is not None:
                        path.append(boxes[priorNode])
                        priorNode = cameFromBack[priorNode]
                    path.append(destination_point)
                    priorNode = cameFromFront[box]
                    while priorNode is not None:
                        path.insert(0,boxes[priorNode])
                        priorNode = cameFromFront[priorNode]
                    path.insert(source_point)
                    return resolvePathfinding(path, boxes)
                estToEnd = math.sqrt((source_point[0] -pathToNew[0]) * (source_point[0] -pathToNew[0]) + (source_point[1] -pathToNew[1]) * (source_point[1] -pathToNew[1]))
                totalCostTo = costToBack[nextNode] + lengthOfPath
                if(box not in cameFromBack or costToBack[box] > totalCostTo  + estToEnd):
                    heappush(toSearch, (totalCostTo + estToEnd, box))
                    cameFromBack[box] = nextNode
                    boxes[box] = pathToNew
                    costToBack[box] = totalCostTo
    if not path:
        return "No Path!"

    #Debug since currently it doesn't draw
    print(path)
#Convert Dijkstra's into A*

#Modify your A* into a Bidirectional A*


#use the shortest_path_to_box function to find the precise path between boxes









    return path, boxes.keys()



#implement the shortest_path_to_box function

def resolvePathfinding(path, boxes):
    if not path:
        return "No Path!"
    print (path)
    return path, boxes.keys()

def shortest_path_to_box(current_point, current_box, new_box):
    """
    new_x1 = new_box[0]
    new_x2 = new_box[1]
    new_y1 = new_box[2]
    new_y2 = new_box[3]

    cur_x1 = current_box[0]
    cur_x2 = current_box[1]
    cur_y1 = current_box[2]
    cur_y2 = current_box[3]


    if(current_point[0] >= new_x2 and current_point[1] >= new_y2):
        return ((new_x2,new_y2))

    if(current_point[0] <= new_x1 and current_point[1] >= new_y2):
        return ((new_x1,new_y2))

    if(current_point[0] <= new_x1 and current_point[1] <= new_y1):
        return ((new_x1,new_y2))

    if(current_point[0] >= new_x2 and current_point[1] <= new_y1):
        return ((new_x2,new_y1))


    if(current_point[0] >= new_x1 and current_point[0] <= new_x2):
        if(current_point[1] >= new_y2):
            return((current_point[0],new_y2))
        else:
            return((current_point[0],new_y1))

    if(current_point[1] >=new_y1 and current_point[1] <=new_y2):
        if(current_point[0] >= new_x2):
            return((new_x2,current_point[1]))
        else:
            return((new_x1,current_point[1]))
    return((0,0))
    """
    xBorder = (max(current_box[0], new_box[0]), min(current_box[1], new_box[1]))
    yBorder = (max(current_box[2], new_box[2]), min(current_box[3], new_box[3]))

    if current_point[0] <= xBorder[0] :
    	returnx = xBorder[0]
    elif current_point[0] <= xBorder[1] :
    	returnx = current_point[0]
    else :
    	returnx = xBorder[1]

    if current_point[1] <= yBorder[0] :
    	returny = yBorder[0]
    elif current_point[1] <= yBorder[1] :
    	returny = current_point[1]
    else :
    	returny = yBorder[1]

    return (returnx, returny)



























