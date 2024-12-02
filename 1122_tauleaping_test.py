# 1122 testing
from tqdm import tqdm

def tau_leaping_simulation_with_progress(params: SimParams, n_runs: int = 1000, checkpoints: list = None) -> np.ndarray:
    """Run multiple tau-leaping simulations with intermediate probability output and a progress bar"""
    time_points = np.arange(0, params.t_max + params.dt, params.dt)
    malignant_counts = np.zeros(len(time_points))
    
    if checkpoints is None:
        checkpoints = []  # Default: no checkpoints
    
    # Initialize tqdm progress bar
    with tqdm(total=n_runs, desc="Simulation Progress") as pbar:
        for run in range(n_runs):
            # Update progress bar
            pbar.update(1)
            
            # Checkpoints output
            if (run + 1) in checkpoints:
                probabilities = malignant_counts / (run + 1)
                print(f"Checkpoint {run + 1}/{n_runs}:")
                print(f"Probabilities: {probabilities}")
                
            # Initialize population dictionary
            population = {State(0, 0, 0): params.N_crypts}
            had_malignant = False
            
            for t_idx, t in enumerate(time_points):
                if had_malignant:
                    malignant_counts[t_idx:] += 1
                    break
                    
                # Process each populated state
                new_events = {}
                for state, count in list(population.items()):
                    if count == 0:
                        continue
                        
                    # Check for division events (negative binomial distribution)
                    division_rate = get_division_rate(state, params)
                    if division_rate > 0:
                        p = np.exp(-division_rate * params.dt)
                        n_divisions = np.random.negative_binomial(count, p)
                        if n_divisions > 0:
                            new_events[state] = new_events.get(state, 0) + n_divisions
                    
                    # Check for transitions to neighbor states
                    for neighbor in get_neighbors(state):
                        rate = get_transition_rate(state, neighbor, params)
                        if rate > 0:
                            # Use Poisson approximation for small rates
                            if rate * params.dt < 0.01:
                                n_transitions = np.random.poisson(rate * params.dt * count)
                            else:
                                # Use binomial for larger rates
                                p = 1 - np.exp(-rate * params.dt)
                                n_transitions = np.random.binomial(count, p)
                                
                            if n_transitions > 0:
                                new_events[state] = new_events.get(state, 0) - n_transitions
                                new_events[neighbor] = new_events.get(neighbor, 0) + n_transitions
                                
                                if neighbor.is_malignant():
                                    had_malignant = True
                                    break
                
                # Update population
                for state, delta in new_events.items():
                    population[state] = population.get(state, 0) + delta
                    if population[state] < 0:  # Sanity check
                        population[state] = 0
                        
                if had_malignant:
                    malignant_counts[t_idx:] += 1
                    break
    
    return malignant_counts / n_runs

# Run the simulation with a progress bar
params = SimParams(
    dt=0.01,           # Time step size
    t_max=80.0,       # Maximum time
    N_crypts=10**8    # Number of initial crypts
)

n_runs = 8000000
checkpoints = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000,
               4500000, 5000000, 5500000, 6000000, 6500000, 7000000, 7500000, 8000000]

time_points = np.arange(0, params.t_max + params.dt, params.dt)
probabilities = tau_leaping_simulation_with_progress(params, n_runs=n_runs, checkpoints=checkpoints)

# Plot the results
plot_results(time_points, probabilities)
