from messaging.Worker import CalculationWorker
import core.keras.Training as tr


def run_app():
    worker = CalculationWorker()

    while True:
        try:
            worker.listen_for_messages()
        except Exception as error:
            pass


tr.setup()
#run_app()