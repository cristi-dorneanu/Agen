from messaging.Worker import CalculationWorker


def run_app():
    worker = CalculationWorker()

    worker.listen_for_messages()

run_app()
