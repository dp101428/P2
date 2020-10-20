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

    #print(mesh)
    startingBox = None
    goalBox = None
    for element in box:
        #print(element)
        if((source_point[0] >= element[0]) and (source_point[0] <= element[1]) and (source_point[1] >= element[2]) and (source_point[1] <= element[3])):
            startingBox = (element)
        if((destination_point[0] >= element[0]) and (destination_point[0] <= element[1]) and (destination_point[1] >= element[2]) and (destination_point[1] <= element[3])):
            goalBox = (element)

    if(startingBox == None or goalBox == None):
        print("No Path")
        return path, boxes.keys()

    #If both the destination and the source are in the same box, shortcut everything
    if(startingBox == goalBox):
        return [source_point, destination_point], [startingBox]






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
        #nextNodeCost is never used, only exists for the heap functions to sort using
        #Find the heuristic from this point to the end
        if(goal == "dest"):
            estToEnd = math.sqrt((destination_point[0] -boxes[nextNode][0]) * (destination_point[0] -boxes[nextNode][0]) + (destination_point[1] -boxes[nextNode][1]) * (destination_point[1] -boxes[nextNode][1]))
        else:
            estToEnd = math.sqrt((source_point[0] -boxes[nextNode][0]) * (source_point[0] -boxes[nextNode][0]) + (source_point[1] -boxes[nextNode][1]) * (source_point[1] -boxes[nextNode][1]))
        
        
        #Keep finding things to put in the queue
        for box in mesh["adj"][nextNode]:
            pathToNew = shortest_path_to_box(boxes[nextNode], nextNode, box, source_point if  goal == "start" else destination_point)
            lengthOfPath = pythagDist(pathToNew[0], pathToNew[1], boxes[nextNode][0], boxes[nextNode][1])
            if (goal == "dest"):
                if(box in costToBack):
                    path.append(pathToNew)
                    #print(goal)
                    #print(boxes[box])
                    #print(boxes[nextNode])
                    path.append(boxes[box])
                    priorNode = cameFromBack[box]
                    while priorNode is not None:
                        path.append(boxes[priorNode])
                        priorNode = cameFromBack[priorNode]
                    #path.append(destination_point)
                    path.insert(0, boxes[nextNode])
                    priorNode = cameFromFront[nextNode]
                    while priorNode is not None:
                        path.insert(0,boxes[priorNode])
                        priorNode = cameFromFront[priorNode]
                    #path.insert(source_point)
                    return resolvePathfinding(path, boxes)
                estToEnd = pythagDist(destination_point[0], destination_point[1], pathToNew[0], pathToNew[1])
                totalCostTo = costToFront[nextNode] + lengthOfPath
                if(box not in cameFromFront or costToFront[box] > totalCostTo +  + estToEnd):
                    heappush(toSearch, (totalCostTo  + estToEnd, box, goal))
                    cameFromFront[box] = nextNode
                    boxes[box] = pathToNew
                    costToFront[box] = totalCostTo
            else:
                if(box in costToFront):
                    path.append(pathToNew)
                    #print(goal)
                    #print(boxes[box])
                    #print(boxes[nextNode])
                    path.append(boxes[nextNode])
                    priorNode = cameFromBack[nextNode]
                    while priorNode is not None:
                        path.append(boxes[priorNode])
                        priorNode = cameFromBack[priorNode]
                    #path.append(destination_point)
                    path.insert(0, boxes[box])
                    priorNode = cameFromFront[box]
                    while priorNode is not None:
                        path.insert(0,boxes[priorNode])
                        priorNode = cameFromFront[priorNode]
                    #path.insert(0, source_point)
                    return resolvePathfinding(path, boxes)
                estToEnd = pythagDist(source_point[0], source_point[1], pathToNew[0], pathToNew[1])
                totalCostTo = costToBack[nextNode] + lengthOfPath
                if(box not in cameFromBack or costToBack[box] > totalCostTo  + estToEnd):
                    heappush(toSearch, (totalCostTo + estToEnd, box, goal))
                    cameFromBack[box] = nextNode
                    boxes[box] = pathToNew
                    costToBack[box] = totalCostTo
    if not path:
        print("No Path")




    return path, boxes.keys()



#implement the shortest_path_to_box function

def resolvePathfinding(path, boxes):
    if not path:
        print ("No Path")
    return path, boxes.keys()

def shortest_path_to_box(current_point, current_box, new_box, goalPoint):
    xBorder = (max(current_box[0], new_box[0]), min(current_box[1], new_box[1]))
    yBorder = (max(current_box[2], new_box[2]), min(current_box[3], new_box[3]))
    #"Simple" version of the algorithm that just finds the shortest path to a new point in the new box
    """
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
    """
    #More complex/overdone algorithm that uses the heuristic for better point selection within the new box
    returnx = -1
    returny = -1
    #If the border is parallel with the x axix, constrain x
    if(xBorder[0] == xBorder[1]):
        returnx = xBorder[0]
    #If the border is parallel with the y axix, constrain y
    if(yBorder[0] == yBorder[1]):
        returny = yBorder[0]
        #If x isn't constrained, evaluate it
        if(returnx != xBorder[0]):
            topEst = pythagDist(current_point[0], current_point[1], xBorder[0], returny) + pythagDist(xBorder[0], returny, goalPoint[0], goalPoint[1])
            bottomEst = pythagDist(current_point[0], current_point[1], xBorder[1], returny) + pythagDist(xBorder[1], returny, goalPoint[0], goalPoint[1])

            if topEst < bottomEst:
                returnx = xBorder[0]
            else:
                returnx = xBorder[1]
            if(returnx != current_point[0] and current_point[0] > xBorder[0] and current_point[0] < xBorder[1]):
                middleEst = pythagDist(current_point[0], current_point[1], current_point[0], returny) + pythagDist(current_point[0], returny, goalPoint[0], goalPoint[1])
                if(middleEst < bottomEst and middleEst < topEst):
                    returnx = current_point[0]
    #If y isn't constrained, evaluate it
    if(returny != yBorder[0]):
        topEst = pythagDist(current_point[0], current_point[1], returnx, yBorder[0]) + pythagDist(returnx, yBorder[0], goalPoint[0], goalPoint[1])
        bottomEst = pythagDist(current_point[0], current_point[1], returnx, yBorder[1]) + pythagDist(returnx, yBorder[1], goalPoint[0], goalPoint[1])

        if topEst < bottomEst:
            returny = yBorder[0]
        else:
            returny = yBorder[1]
        if(returny != current_point[1] and current_point[1] > yBorder[0] and current_point[1] < yBorder[1]):
            middleEst = pythagDist(current_point[0], current_point[1], returnx, current_point[1]) + pythagDist(returnx, current_point[1], goalPoint[0], goalPoint[1])
            if(middleEst < bottomEst and middleEst < topEst):
                returny = current_point[1]
    #Theoretically the closest point to the destination could be none of these (directly in line with the destination) but that will probably be rare and this is long enough
    return (returnx, returny)


def pythagDist(x0,y0, x1, y1):
    return (math.sqrt((x1-x0) * (x1-x0) + (y1-y0) * (y1-y0)))
