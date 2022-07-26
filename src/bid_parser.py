import openrtb_pb2 as openrtbBid
import realtime_bidding_proto_pb2 as googleBid
from google.protobuf import text_format as tf
from google.protobuf import json_format as jf


def parse(protocol, str_):
    try:
        if protocol == 'Openrtb':
            b = jf.Parse(jf.MessageToJson(str_), openrtbBid.BidRequest())
            return b.SerializeToString()
        b = tf.Parse(str_, googleBid.BidRequest)
        return b.SerializeToString()
    except Exception as e:
        print(e)
        return None,e