from messaging.Worker import CalculationWorker


def run_app():
    worker = CalculationWorker()

    while True:
        try:
            worker.listen_for_messages()
        except Exception as error:
            print(error)


run_app()