import mlflow
import pytest

from rlstack import RecurrentTrainer, Trainer
from rlstack.env import DiscreteDummyEnv

NUM_ENVS = 64
HORIZON = 32
HORIZONS_PER_ENV_RESET = 2


@pytest.fixture(autouse=True)
def run() -> None:
    active_run = mlflow.start_run(run_name="test_trainers")
    yield active_run
    mlflow.end_run()
    mlflow.delete_run(active_run.info.run_id)


def test_feedforward_trainer_eval() -> None:
    trainer = Trainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0

    trainer.eval()
    assert trainer.state["algorithm/collects"] == HORIZONS_PER_ENV_RESET
    assert trainer.state["algorithm/steps"] == 0


def test_feedforward_trainer_eval_runtime_error() -> None:
    trainer = Trainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0
    trainer.step()

    with pytest.raises(RuntimeError):
        trainer.eval()


def test_feedforward_trainer_step() -> None:
    trainer = Trainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0

    trainer.step()
    assert trainer.state["algorithm/collects"] == 1
    assert trainer.state["algorithm/steps"] == 1


def test_feedforward_trainer_run() -> None:
    ...


def test_recurrent_trainer_eval() -> None:
    trainer = RecurrentTrainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0

    trainer.eval()
    assert trainer.state["algorithm/collects"] == HORIZONS_PER_ENV_RESET
    assert trainer.state["algorithm/steps"] == 0


def test_recurrent_trainer_eval_runtime_error() -> None:
    trainer = RecurrentTrainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0
    trainer.step()

    with pytest.raises(RuntimeError):
        trainer.eval()


def test_recurrent_trainer_step() -> None:
    trainer = RecurrentTrainer(
        DiscreteDummyEnv,
        num_envs=NUM_ENVS,
        horizon=HORIZON,
        horizons_per_env_reset=HORIZONS_PER_ENV_RESET,
    )
    assert trainer.state["algorithm/collects"] == 0
    assert trainer.state["algorithm/steps"] == 0
    assert trainer.state["env/steps"] == 0

    trainer.step()
    assert trainer.state["algorithm/collects"] == 1
    assert trainer.state["algorithm/steps"] == 1


def test_recurrent_trainer_run() -> None:
    ...
