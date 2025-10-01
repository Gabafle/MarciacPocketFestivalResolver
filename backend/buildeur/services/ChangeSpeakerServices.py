from backend.buildeur.utils import BuilderUtils
from backend.structure.Speaker import Speaker


class changeSpeakerService:

    def __init__(self, party):
        self.party = party

    def change_speaker(self, number_speaker):
        speaker_count = self.party.elements.count(Speaker())
        speaker_max = Speaker().max
        speaker_min = Speaker().min

        if number_speaker < speaker_min:
            number_speaker = speaker_min

        if number_speaker > speaker_max:
            number_speaker = speaker_max

        if number_speaker > speaker_count:
            self.add_speaker(number_speaker, speaker_count)

        if number_speaker < speaker_count:
            self.remove_speaker(number_speaker)

    def remove_speaker(self, number_speaker):
        BuilderUtils(self.party).remove_element(number_speaker, Speaker)

    def add_speaker(self, number_speaker, speaker_count):
        BuilderUtils(self.party).add_element(number_speaker, speaker_count, Speaker)
