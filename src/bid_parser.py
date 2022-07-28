import openrtb_pb2 as openrtbBid
import realtime_bidding_proto_pb2 as googleBid
# from google.protobuf import text_format as tf
from google.protobuf import json_format as jf
import requests
import json


def parse(protocol, str_):
    # print(type(str_))
    try:
        if protocol == 'Openrtb':
            import json
            c = json.loads(str_)
            # print(type(c))
            b = jf.ParseDict(c, openrtbBid.BidRequest())
            # from here call send_bid
            return b.SerializeToString()
        else:
            b = jf.ParseDict(str_, googleBid.BidRequest())
            return b.SerializeToString()
    except Exception as e:
        return None, str(e)


def send_bid(stream, exchange):
    try:
        config = open('../config.json')
        file_ = config.read()
        config = json.loads(file_)
        if config.get("endpoint") and config.get("method"):
            # TODO : require changes
            out = requests.post(f"{config['endpoint']}/{exchange}", data=stream)
            return out.json()
        raise Exception
    except Exception as e:
        print(e)
        return None, str(e)


if __name__ == '__main__':
    send_bid(None, None)