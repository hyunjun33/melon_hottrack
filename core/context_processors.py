from django.contrib import messages


def lazy_messages_list(request):
    # 장고 템플릿에서는 인자 없는 함수를 호출할 수 있다.
    # 아래 messages_list 함수에서 dictionary를 만들 때
    # 메세지 목록을 가져오는 것이 아니라, 메세지를 소비하는 시점에 메세지를 가져오도록 지연시키는 함수

    def inner():
        message_list = messages.get_messages(request)

        # 변환이 가능한 타입인 리스트와 사전으로 먼저 변환
        return [
            {
                "level_tag": message.level_tag,
                "message": message.message,
            }
            for message in message_list
        ]

    return inner


def messages_list(request):
    return {
        "messages_list": lazy_messages_list(request),
    }
