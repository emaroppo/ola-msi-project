from environments.ns_environment import SocialNChanges
from learners.ucb_learners.ucb_prob_learner import UCBProbLearner
from learners.ucb_learners.ns_ucb import SWUCBProbLearner, CDUCBProbLearner
from utils.simulation import influence_simulation


def sensitivity_analysis(model, parameters_value, env, n_episodes=365):
    models = model.sensitivity_analysis(parameters=parameters_value)
    metrics, models = influence_simulation(
        models=models, env=env, n_episodes=n_episodes
    )
    return metrics, models, env


def step_5(graph_probabilities, graph_structure, n_phases=3, n_episodes=365):
    env = SocialNChanges(graph_probabilities, n_phases=n_phases)
    # initialise bandit
    model1 = UCBProbLearner(30, 3, graph_structure=graph_structure)
    model2 = SWUCBProbLearner(30, 3, 121, graph_structure=graph_structure)
    model3 = CDUCBProbLearner(30, 3, graph_structure=graph_structure)

    # run simulation
    metrics, models = influence_simulation(
        env, [model1, model2, model3], n_episodes=n_episodes, n_phases=n_phases
    )

    # check different window sizes

    window_sizes = [60, 90, 120]
    metrics1, models1 = sensitivity_analysis(SWUCBProbLearner, window_sizes)

    # check different eps values

    eps_values = [0.02, 0.05, 0.07]
    metrics2, models2 = sensitivity_analysis(CDUCBProbLearner, eps_values)

    return metrics