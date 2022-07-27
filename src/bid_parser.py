import openrtb_pb2 as openrtbBid
import realtime_bidding_proto_pb2 as googleBid
# from google.protobuf import text_format as tf
from google.protobuf import json_format as jf


def parse(protocol, str_):
    print(type(str_))
    try:
        if protocol == 'Openrtb':
            import json
            c = json.loads(str_)
            print(type(c))
            b = jf.ParseDict(c, openrtbBid.BidRequest())
            return b.SerializeToString()
        else:
            b = jf.ParseDict(str_, googleBid.BidRequest)
            return b.SerializeToString()
    except Exception as e:
        return None, str(e)