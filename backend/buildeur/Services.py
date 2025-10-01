from backend.buildeur.services.ChangeBodyGuardServices import changeBodyGuardServices
from backend.buildeur.services.ChangeChairServices import changeChairService
from backend.buildeur.services.ChangeSpeakerServices import changeSpeakerService
from backend.buildeur.services.ChangeStandServices import changeStandService
from backend.buildeur.services.ChangeTentServices import changeTentService
from backend.buildeur.services.ChangeToiletService import changeToiletService
from backend.buildeur.services.ChangeVendingMachineService import (
    changeVendingMachineService,
)
from backend.buildeur.services.ChangeWaterFontainService import (
    changeWaterFontainService,
)


class Services:
    def __init__(self, party):
        self.stand_services = changeStandService(party)
        self.bodyguard_services = changeBodyGuardServices(party)
        self.chair_services = changeChairService(party)
        self.speaker_services = changeSpeakerService(party)
        self.tent_services = changeTentService(party)
        self.toilet_services = changeToiletService(party)
        self.vending_machine_services = changeVendingMachineService(party)
        self.water_fontain_services = changeWaterFontainService(party)
