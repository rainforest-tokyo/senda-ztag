# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import anonstore_pb2 as anonstore__pb2
import hoststore_pb2 as hoststore__pb2
import rpc_pb2 as rpc__pb2


class AdminServiceStub(object):
  """Two gRPC interfaces. One from

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Shutdown = channel.unary_unary(
        '/zsearch.AdminService/Shutdown',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.Status = channel.unary_unary(
        '/zsearch.AdminService/Status',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.Statistics = channel.unary_unary(
        '/zsearch.AdminService/Statistics',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.PruneIPv4 = channel.unary_unary(
        '/zsearch.AdminService/PruneIPv4',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.PruneDomain = channel.unary_unary(
        '/zsearch.AdminService/PruneDomain',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.UpdateASData = channel.unary_unary(
        '/zsearch.AdminService/UpdateASData',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.UpdateLocationData = channel.unary_unary(
        '/zsearch.AdminService/UpdateLocationData',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.ValidateCertificates = channel.unary_unary(
        '/zsearch.AdminService/ValidateCertificates',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.FixCertificateSource = channel.unary_unary(
        '/zsearch.AdminService/FixCertificateSource',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.DumpIPv4ToJSON = channel.unary_unary(
        '/zsearch.AdminService/DumpIPv4ToJSON',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.DumpDomainToJSON = channel.unary_unary(
        '/zsearch.AdminService/DumpDomainToJSON',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.DumpCertificatesToJSON = channel.unary_unary(
        '/zsearch.AdminService/DumpCertificatesToJSON',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.DumpKeysToJSON = channel.unary_unary(
        '/zsearch.AdminService/DumpKeysToJSON',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.RegenerateIPv4Deltas = channel.unary_unary(
        '/zsearch.AdminService/RegenerateIPv4Deltas',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.RegenerateDomainDeltas = channel.unary_unary(
        '/zsearch.AdminService/RegenerateDomainDeltas',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.RegenerateCertificateDeltas = channel.unary_unary(
        '/zsearch.AdminService/RegenerateCertificateDeltas',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.RegenerateSingleCertificateDelta = channel.unary_unary(
        '/zsearch.AdminService/RegenerateSingleCertificateDelta',
        request_serializer=rpc__pb2.AnonymousQuery.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.ReprocessCertificates = channel.unary_unary(
        '/zsearch.AdminService/ReprocessCertificates',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.ReprocessSingleCertificate = channel.unary_unary(
        '/zsearch.AdminService/ReprocessSingleCertificate',
        request_serializer=rpc__pb2.AnonymousQuery.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.Ping = channel.unary_unary(
        '/zsearch.AdminService/Ping',
        request_serializer=rpc__pb2.Command.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )


class AdminServiceServicer(object):
  """Two gRPC interfaces. One from

  """

  def Shutdown(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Statistics(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PruneIPv4(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PruneDomain(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateASData(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLocationData(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidateCertificates(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FixCertificateSource(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DumpIPv4ToJSON(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DumpDomainToJSON(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DumpCertificatesToJSON(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DumpKeysToJSON(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegenerateIPv4Deltas(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegenerateDomainDeltas(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegenerateCertificateDeltas(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegenerateSingleCertificateDelta(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReprocessCertificates(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReprocessSingleCertificate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Shutdown': grpc.unary_unary_rpc_method_handler(
          servicer.Shutdown,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'Statistics': grpc.unary_unary_rpc_method_handler(
          servicer.Statistics,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'PruneIPv4': grpc.unary_unary_rpc_method_handler(
          servicer.PruneIPv4,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'PruneDomain': grpc.unary_unary_rpc_method_handler(
          servicer.PruneDomain,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'UpdateASData': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateASData,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'UpdateLocationData': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLocationData,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'ValidateCertificates': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateCertificates,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'FixCertificateSource': grpc.unary_unary_rpc_method_handler(
          servicer.FixCertificateSource,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'DumpIPv4ToJSON': grpc.unary_unary_rpc_method_handler(
          servicer.DumpIPv4ToJSON,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'DumpDomainToJSON': grpc.unary_unary_rpc_method_handler(
          servicer.DumpDomainToJSON,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'DumpCertificatesToJSON': grpc.unary_unary_rpc_method_handler(
          servicer.DumpCertificatesToJSON,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'DumpKeysToJSON': grpc.unary_unary_rpc_method_handler(
          servicer.DumpKeysToJSON,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'RegenerateIPv4Deltas': grpc.unary_unary_rpc_method_handler(
          servicer.RegenerateIPv4Deltas,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'RegenerateDomainDeltas': grpc.unary_unary_rpc_method_handler(
          servicer.RegenerateDomainDeltas,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'RegenerateCertificateDeltas': grpc.unary_unary_rpc_method_handler(
          servicer.RegenerateCertificateDeltas,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'RegenerateSingleCertificateDelta': grpc.unary_unary_rpc_method_handler(
          servicer.RegenerateSingleCertificateDelta,
          request_deserializer=rpc__pb2.AnonymousQuery.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'ReprocessCertificates': grpc.unary_unary_rpc_method_handler(
          servicer.ReprocessCertificates,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'ReprocessSingleCertificate': grpc.unary_unary_rpc_method_handler(
          servicer.ReprocessSingleCertificate,
          request_deserializer=rpc__pb2.AnonymousQuery.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=rpc__pb2.Command.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'zsearch.AdminService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class QueryServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetHostIPv4Record = channel.unary_unary(
        '/zsearch.QueryService/GetHostIPv4Record',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=rpc__pb2.HostQueryResponse.FromString,
        )
    self.PutHostIPv4Record = channel.unary_unary(
        '/zsearch.QueryService/PutHostIPv4Record',
        request_serializer=hoststore__pb2.Record.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.DelHostIPv4Record = channel.unary_unary(
        '/zsearch.QueryService/DelHostIPv4Record',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.GetAllIPv4Records = channel.unary_unary(
        '/zsearch.QueryService/GetAllIPv4Records',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=rpc__pb2.HostQueryResponse.FromString,
        )
    self.GetHostIPv4Delta = channel.unary_unary(
        '/zsearch.QueryService/GetHostIPv4Delta',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.GetHostDomainRecord = channel.unary_unary(
        '/zsearch.QueryService/GetHostDomainRecord',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=rpc__pb2.HostQueryResponse.FromString,
        )
    self.PutHostDomainRecord = channel.unary_unary(
        '/zsearch.QueryService/PutHostDomainRecord',
        request_serializer=hoststore__pb2.Record.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.DelHostDomainRecord = channel.unary_unary(
        '/zsearch.QueryService/DelHostDomainRecord',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.GetAllDomainRecords = channel.unary_unary(
        '/zsearch.QueryService/GetAllDomainRecords',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=rpc__pb2.HostQueryResponse.FromString,
        )
    self.GetHostDomainDelta = channel.unary_unary(
        '/zsearch.QueryService/GetHostDomainDelta',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Delta.FromString,
        )
    self.GetCertificate = channel.unary_unary(
        '/zsearch.QueryService/GetCertificate',
        request_serializer=rpc__pb2.AnonymousQuery.SerializeToString,
        response_deserializer=rpc__pb2.AnonymousQueryResponse.FromString,
        )
    self.UpsertCertificate = channel.unary_unary(
        '/zsearch.QueryService/UpsertCertificate',
        request_serializer=anonstore__pb2.AnonymousRecord.SerializeToString,
        response_deserializer=anonstore__pb2.AnonymousDelta.FromString,
        )
    self.UpsertRawCertificate = channel.unary_unary(
        '/zsearch.QueryService/UpsertRawCertificate',
        request_serializer=anonstore__pb2.AnonymousRecord.SerializeToString,
        response_deserializer=anonstore__pb2.AnonymousDelta.FromString,
        )
    self.GetCryptographicKey = channel.unary_unary(
        '/zsearch.QueryService/GetCryptographicKey',
        request_serializer=rpc__pb2.AnonymousQuery.SerializeToString,
        response_deserializer=rpc__pb2.AnonymousQueryResponse.FromString,
        )
    self.UpsertCryptographicKey = channel.unary_unary(
        '/zsearch.QueryService/UpsertCryptographicKey',
        request_serializer=anonstore__pb2.AnonymousRecord.SerializeToString,
        response_deserializer=anonstore__pb2.AnonymousDelta.FromString,
        )
    self.GetPublicLocation = channel.unary_unary(
        '/zsearch.QueryService/GetPublicLocation',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.LocationAtom.FromString,
        )
    self.GetRestrictedLocation = channel.unary_unary(
        '/zsearch.QueryService/GetRestrictedLocation',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.LocationAtom.FromString,
        )
    self.GetWHOIS = channel.unary_unary(
        '/zsearch.QueryService/GetWHOIS',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Record.FromString,
        )
    self.GetUserMetadata = channel.unary_unary(
        '/zsearch.QueryService/GetUserMetadata',
        request_serializer=rpc__pb2.HostQuery.SerializeToString,
        response_deserializer=hoststore__pb2.Record.FromString,
        )
    self.PutUserMetadata = channel.unary_unary(
        '/zsearch.QueryService/PutUserMetadata',
        request_serializer=hoststore__pb2.Record.SerializeToString,
        response_deserializer=rpc__pb2.CommandReply.FromString,
        )
    self.GetRootStore = channel.unary_unary(
        '/zsearch.QueryService/GetRootStore',
        request_serializer=rpc__pb2.RootStoreQuery.SerializeToString,
        response_deserializer=rpc__pb2.RootStoreReply.FromString,
        )


class QueryServiceServicer(object):

  def GetHostIPv4Record(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutHostIPv4Record(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelHostIPv4Record(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllIPv4Records(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHostIPv4Delta(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHostDomainRecord(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutHostDomainRecord(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelHostDomainRecord(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllDomainRecords(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHostDomainDelta(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCertificate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpsertCertificate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpsertRawCertificate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCryptographicKey(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpsertCryptographicKey(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPublicLocation(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRestrictedLocation(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWHOIS(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserMetadata(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutUserMetadata(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRootStore(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetHostIPv4Record': grpc.unary_unary_rpc_method_handler(
          servicer.GetHostIPv4Record,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=rpc__pb2.HostQueryResponse.SerializeToString,
      ),
      'PutHostIPv4Record': grpc.unary_unary_rpc_method_handler(
          servicer.PutHostIPv4Record,
          request_deserializer=hoststore__pb2.Record.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'DelHostIPv4Record': grpc.unary_unary_rpc_method_handler(
          servicer.DelHostIPv4Record,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'GetAllIPv4Records': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllIPv4Records,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=rpc__pb2.HostQueryResponse.SerializeToString,
      ),
      'GetHostIPv4Delta': grpc.unary_unary_rpc_method_handler(
          servicer.GetHostIPv4Delta,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'GetHostDomainRecord': grpc.unary_unary_rpc_method_handler(
          servicer.GetHostDomainRecord,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=rpc__pb2.HostQueryResponse.SerializeToString,
      ),
      'PutHostDomainRecord': grpc.unary_unary_rpc_method_handler(
          servicer.PutHostDomainRecord,
          request_deserializer=hoststore__pb2.Record.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'DelHostDomainRecord': grpc.unary_unary_rpc_method_handler(
          servicer.DelHostDomainRecord,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'GetAllDomainRecords': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllDomainRecords,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=rpc__pb2.HostQueryResponse.SerializeToString,
      ),
      'GetHostDomainDelta': grpc.unary_unary_rpc_method_handler(
          servicer.GetHostDomainDelta,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Delta.SerializeToString,
      ),
      'GetCertificate': grpc.unary_unary_rpc_method_handler(
          servicer.GetCertificate,
          request_deserializer=rpc__pb2.AnonymousQuery.FromString,
          response_serializer=rpc__pb2.AnonymousQueryResponse.SerializeToString,
      ),
      'UpsertCertificate': grpc.unary_unary_rpc_method_handler(
          servicer.UpsertCertificate,
          request_deserializer=anonstore__pb2.AnonymousRecord.FromString,
          response_serializer=anonstore__pb2.AnonymousDelta.SerializeToString,
      ),
      'UpsertRawCertificate': grpc.unary_unary_rpc_method_handler(
          servicer.UpsertRawCertificate,
          request_deserializer=anonstore__pb2.AnonymousRecord.FromString,
          response_serializer=anonstore__pb2.AnonymousDelta.SerializeToString,
      ),
      'GetCryptographicKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetCryptographicKey,
          request_deserializer=rpc__pb2.AnonymousQuery.FromString,
          response_serializer=rpc__pb2.AnonymousQueryResponse.SerializeToString,
      ),
      'UpsertCryptographicKey': grpc.unary_unary_rpc_method_handler(
          servicer.UpsertCryptographicKey,
          request_deserializer=anonstore__pb2.AnonymousRecord.FromString,
          response_serializer=anonstore__pb2.AnonymousDelta.SerializeToString,
      ),
      'GetPublicLocation': grpc.unary_unary_rpc_method_handler(
          servicer.GetPublicLocation,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.LocationAtom.SerializeToString,
      ),
      'GetRestrictedLocation': grpc.unary_unary_rpc_method_handler(
          servicer.GetRestrictedLocation,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.LocationAtom.SerializeToString,
      ),
      'GetWHOIS': grpc.unary_unary_rpc_method_handler(
          servicer.GetWHOIS,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Record.SerializeToString,
      ),
      'GetUserMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserMetadata,
          request_deserializer=rpc__pb2.HostQuery.FromString,
          response_serializer=hoststore__pb2.Record.SerializeToString,
      ),
      'PutUserMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.PutUserMetadata,
          request_deserializer=hoststore__pb2.Record.FromString,
          response_serializer=rpc__pb2.CommandReply.SerializeToString,
      ),
      'GetRootStore': grpc.unary_unary_rpc_method_handler(
          servicer.GetRootStore,
          request_deserializer=rpc__pb2.RootStoreQuery.FromString,
          response_serializer=rpc__pb2.RootStoreReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'zsearch.QueryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
