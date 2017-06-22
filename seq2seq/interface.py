from seq2seq import execute, data_utils
import tensorflow as tf
import os
import numpy as np
import sys


sess = tf.Session()
gConfig = execute.get_config()
model = execute.create_model(sess, True)
model.batch_size = 1
enc_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d.enc" % gConfig['enc_vocab_size'])
#dec_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d.dec" % gConfig['dec_vocab_size'])
enc_vocab, rev_enc_vocab = data_utils.initialize_vocabulary(enc_vocab_path)
#_, rev_dec_vocab = data_utils.initialize_vocabulary(dec_vocab_path)
_buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]


def get_response(user_input):
    """user_input is a SpaCy doc."""
    # Get token-ids for the input sentence.
    sentence = user_input.text
    print(sentence)
    #token_ids = data_utils.sentence_to_token_ids(tf.compat.as_bytes(sentence),
    #                                             enc_vocab,
    #                                             normalize_digits=False)
    tokens = data_utils.basic_tokenizer(tf.compat.as_bytes(sentence))
    token_ids = [enc_vocab[t.decode('utf-8')] for t in tokens]
    print(token_ids)
    # Which bucket does it belong to?
    bucket_id = min([b for b in range(len(_buckets))
                     if _buckets[b][0] > len(token_ids)])
    # Get a 1-element batch to feed the sentence to the model.
    encoder_inputs, decoder_inputs, target_weights = model.get_batch(
        {bucket_id: [(token_ids, [])]}, bucket_id)
    # Get output logits for the sentence.
    _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                     target_weights, bucket_id, True)
    # This is a greedy decoder - outputs are just argmaxes of output_logits.
    outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
    # If there is an EOS symbol in outputs, cut them at that point.
    if data_utils.EOS_ID in outputs:
        outputs = outputs[:outputs.index(data_utils.EOS_ID)]
    print('Outputs:')
    print(outputs)
    print([rev_enc_vocab[output] for output in outputs])
    return ' '.join([rev_enc_vocab[output] for output in outputs])
    #result = " ".join(
    #    [tf.compat.as_str(rev_enc_vocab[output]) for output in outputs])
