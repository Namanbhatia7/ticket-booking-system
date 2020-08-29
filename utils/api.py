from flask import (
  request
)

from flask_restx import (
  Api,
  fields,
  Namespace,
  Resource,
  reqparse
)

from utils.models import RequestModels

# set apiAuth to False if you want to test without auth-token
apiAuth = False
xAuthToken = '123xyz'

api = Namespace('api', description='Booking and Tickets related methods.')

# importing all request models
RequestModel = RequestModels(api)
BookTicketModel = RequestModel.BookTicketModel()
UpdateTimingModel = RequestModel.UpdateTimingModel()
ViewAllTicketModel = RequestModel.ViewAllTicketModel()
UserDetailsModel = RequestModel.UserDetailsModel()
DeleteTicketModel = RequestModel.DeleteTicketModel()
MarkTicketExpireModel = RequestModel.MarkTicketExpireModel()


@api.route('/book-ticket')
class BookTicket(Resource):
  
  @api.expect(BookTicketModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/update-timing')
class UpdateTiming(Resource):

  @api.expect(UpdateTimingModel)
  def put(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200


@api.route('/view-all-tickets')
class ViewAllTickets(Resource):

  @api.expect(ViewAllTicketModel)
  def get(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/delete-ticket')
class DeleteTicket(Resource):

  @api.expect(DeleteTicketModel)
  def delete  (self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/user-details')
class DeleteTicket(Resource):

  @api.expect(UserDetailsModel)
  def get(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/mark-expire')
class MarkTicketExpire(Resource):

  @api.expect(MarkTicketExpireModel)
  def put(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200