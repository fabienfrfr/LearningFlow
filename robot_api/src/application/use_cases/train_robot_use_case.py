import mlflow
import mlflow.pytorch
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

class TrainRobotModelUseCase:
    def __init__(self, model_name: str, dataset_name: str):
        self.model_name = model_name
        self.dataset_name = dataset_name

    def execute(self):
        # Load dataset
        dataset = load_dataset(self.dataset_name)

        # Load model
        model = AutoModelForSequenceClassification.from_pretrained(self.model_name)

        # Define training arguments
        training_args = TrainingArguments(
            output_dir="./results",
            evaluation_strategy="epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=3,
            weight_decay=0.01,
        )

        # Define trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["test"],
        )

        # Train the model
        trainer.train()

        # Log the model with MLflow
        with mlflow.start_run():
            mlflow.pytorch.log_model(model, "huggingface_robot_model")
            mlflow.log_params(training_args.to_dict())
            mlflow.log_metrics({"train_loss": trainer.state.log_history[-1]["loss"]})

        return trainer.state.log_history

