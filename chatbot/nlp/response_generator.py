from chatbot.common.chat_share_data import ShareData

class ResponseGenerator(ShareData):
    """

    """
    def select_response(self, share_data):
        try:
            self.__dict__ = share_data.__dict__
            response = ""
            if (self.story_board_id == '1'):
                self.set_output_data("이미지 검색 결과 출력")
            elif (self.story_board_id == '2'):
                response = self.story_slot_entity["이름"] + "의 전화번호는 XX-XXX-1234입니다."
            elif (self.story_board_id == '3'):
                name = self.story_slot_entity["업무"]
                business = {"출하" : "김승우", "야드" : "김수상", "설비" : "박성찬", "매출" : "백지현", "공정" : "이상현", "원가" : "김영재"}
                response = self.story_slot_entity["업무"] + "업무 담당자는" + business[name] + "입니다"
            elif (self.story_board_id == '4'):
                response = self.story_slot_entity["이름"] + "은 " + self.story_slot_entity["날짜"] + " 휴가입니다."
            elif (self.story_board_id == '5'):
                response = "AI과제 맴버는 김승우, 김수상, 백지현, 박성찬, 김영재, 이태영, 황민호, 이상현입니다."
            elif (self.story_board_id == '6'):
                name = self.story_slot_entity["이름"]
                leader = {"김수상": "김영식", "김승우": "김영식", "차민주": "박종규", "박종규": "김채홍", "신민호": "김동희", "김동희": "주용회", "주용회": "박미화"}
                response = self.story_slot_entity["이름"] + "님의 팀장은 " + leader[name] + "입니다"
            elif (self.story_board_id == '7'):
                response = self.story_slot_entity["이름"] + " 등 X명이 참석자로 " + self.story_slot_entity["장소"] + "에서 회의 예약 되었습니다."
            else :
                response = self.get_unknown_response()
            print("■■■■■■■■■■ 챗봇 응답 메세지 결과 : " + response)
            self.set_output_data(response)
            #share_data = self._initailize_story(share_data)
            self.initialize_story()
            share_data.__dict__ =  self.__dict__
            return share_data

        except Exception as e:
            raise Exception(e)

    def _initailize_story(self, share_data):

        if(share_data != None) :
            share_data.set_story_id("")
            share_data.set_intent_id("")
            share_data.set_request_data("")
            share_data.initialize_story_slot_entity()
            share_data.set_request_type("")
        return share_data

    def get_unknown_response(self) :
        return "무슨 말씀인지 잘 모르겠어요"

    def tone_generator(self):
        return None

    def grammar_generator(self):
        return None

    def final_generator(self):
        response = 'Hi I am Bot'
        return response