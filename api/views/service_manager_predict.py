import json
from rest_framework.response import Response
from rest_framework.views import APIView
from cluster.service.service_predict_d2v import PredictNetD2V
from cluster.service.service_predict_w2v import PredictNetW2V
from cluster.service.service_predict_cnn import PredictNetCnn
from cluster.service.service_predict_renet import PredictNetRenet
from cluster.service.service_predict_wdnn import PredictNetWdnn
from cluster.service.service_predict_seq2seq import PredictNetSeq2Seq
from cluster.service.service_predict_autoencoder import PredictNetAutoEncoder
from cluster.service.service_predict_anomaly import PredictNetAnomaly
from cluster.service.service_predict_wcnn import PredictNetWcnn
from cluster.service.service_predict_bilstmcrf import PredictNetBiLstmCrf
from common.utils import *
import coreapi

class ServiceManagerPredict(APIView):
    # TODO:add document sample for swagger (need to update)
    coreapi_fields = (
        coreapi.Field(
            name='parm1',
            required=True,
            type='string',
        ),
        coreapi.Field(
            name='parm2',
            required=True,
            type='string',
        ),
    )
    def post(self, request, type, nnid, ver):
        """
        - desc : insert cnn configuration data
        """
        try:
            if(ver == 'active') :
                if(type == 'w2v') :
                    return_data = PredictNetW2V().run(nnid, request.data)
                elif(type == "d2v"):
                    return_data = PredictNetD2V().run(nnid, request.data)
                elif(type == "cnn"):
                    # TO-DO : need predict function for active taged version
                    raise Exception("on developing now !")
                elif (type == "wdnn"):
                    return_data = PredictNetWdnn().run(nnid, ver, request.FILES)
                elif(type == "seq2seq"):
                    return_data = PredictNetSeq2Seq().run(nnid, request.data)
                elif(type == "autoencoder"):
                    return_data = PredictNetAutoEncoder().run(nnid, request.data)
                elif (type == "renet"):
                    #return_data = PredictNetRenet().run(nnid, ver, request.FILES)
                    # TO-DO : need to create PredictNetRenet class first
                    raise Exception("on developing now !")
                elif (type == "anomaly"):
                    return_data = PredictNetAnomaly().run(nnid, request.data)
                elif (type == "wcnn"):
                    return_data = PredictNetWcnn().run(nnid, request.data)
                elif (type == "bilstmcrf"):
                    return_data = PredictNetBiLstmCrf().run(nnid, request.data)
                else :
                    raise Exception ("Not defined type error")
            else :
                if (type == 'w2v'):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "d2v"):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "cnn"):
                    return_data = PredictNetCnn().run(nnid, ver, request.FILES)
                elif (type == "wdnn"):
                    return_data = PredictNetWdnn().run(nnid, ver, request.FILES)
                elif (type == "seq2seq"):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "renet"):
                    return_data = PredictNetRenet().run(nnid, ver, request.FILES)
                else:
                    raise Exception("Not defined type error")

            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, type, nnid, ver):
        """
        - desc : get cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, type, nnid, ver):
        """
        - desc ; update cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, type, nnid, ver):
        """
        - desc : delete cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))