from django.shortcuts import render
from .algorithm import PathfindingProblem, Node, expand, path_states, a_star, heuristic

boroughs = {
    'Camden': [51.5290, -0.1255],
    'Greenwich': [51.4892, 0.0648],
    'Hackney': [51.5450, -0.0554],
    'Hammersmith': [51.4928, -0.2230],
    'Islington': [51.5380, -0.1030],
    'Kensington': [51.5010, -0.1930],
    'Lambeth': [51.4654, -0.1136],
    'Lewisham': [51.4522, -0.0148],
    'Southwark': [51.5035, -0.0804],
    'Westminster': [51.4975, -0.1357]
}

neighbors = {
    'Camden': ['Islington', 'Westminster', 'Southwark'],
    'Greenwich': ['Lewisham', 'Southwark'],
    'Hackney': ['Islington'],
    'Hammersmith': ['Kensington', 'Westminster'],
    'Islington': ['Camden', 'Hackney', 'Westminster'],
    'Kensington': ['Hammersmith', 'Westminster'],
    'Lambeth': ['Southwark', 'Lewisham', 'Westminster'],
    'Lewisham': ['Greenwich', 'Lambeth'],
    'Southwark': ['Camden', 'Greenwich', 'Lambeth', 'Westminster'],
    'Westminster': ['Camden', 'Islington', 'Hammersmith', 'Kensington', 'Lambeth', 'Southwark']
}

def index(request):
    return render(request, 'newapp/index.html', {'boroughs': boroughs.keys()})

def ai_index(request):
    if request.method == 'POST':
        initial = request.POST.get('initial_state', 'Camden')
        goal = request.POST.get('goal_state', 'Greenwich')

        print(f"Initial: {initial}, Goal: {goal}")  # Debugging line

        problem = PathfindingProblem(initial=initial, goal=goal)
        solution = a_star(problem, boroughs, neighbors)

        path = path_states(solution) if solution else []
        print(f"Path: {path}")  # Debugging line

        # Generate polyline data using the path found by A* algorithm
        polyline = [boroughs[state] for state in path]
        print(f"Polyline: {polyline}")  # Debugging line

        context = {
            'path': path,
            'polyline': polyline,
            'initial': initial,
            'goal': goal,
            'boroughs': boroughs
        }

        return render(request, 'newapp/ai_results.html', context)
    else:
        return render(request, 'newapp/ai_index.html', {'boroughs': boroughs.keys()})
