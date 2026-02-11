from jiwer import wer, cer

def evaluate(predicted, reference):
    return {
        "WER": wer(reference, predicted),
        "CER": cer(reference, predicted)
    }
