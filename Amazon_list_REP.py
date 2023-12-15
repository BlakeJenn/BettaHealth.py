import zmq
import json


class Reply:
    def __init__(self, socket, filepath):
        self.socket = socket
        self.treatment_links = {}
        with open(filepath) as infile:
            self.treatment_links = json.load(infile)

    def get_treatment_links(self, disease):
        if disease in self.treatment_links:
            return self.treatment_links[disease]
        else:
            return "Disease not found in treatment dictionary."

    def reply_link(self):
        while True:
            disease = self.socket.recv_string()
            treatment_links = self.get_treatment_links(disease)
            self.socket.send_pyobj(treatment_links)

    def handle_reply(self):
        # wrapper
        self.reply_link()


socket = zmq.Context().socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5500")
reply = Reply(socket, "treatment_links.json")
reply.handle_reply()

