from qgis.core import QgsProcessingProvider
from PyQt5.QtGui import QIcon
import os

#import algorithm
#from .fileslist import Files2Table
from .update_ear import UpdateEar
from .update_zkn import UpdateZkn
from .seznam_parcel import SeznamParcelZnotrajObmojaRaziskave
from .download_lidar import DownloadLidar
from .load_presets import LoadPreset
from pathlib import Path
from ..general_modules import (path             
                        )

class Provider(QgsProcessingProvider):
    def __init__(self):
        self.plugin_dir = os.path.dirname(__file__)
        QgsProcessingProvider.__init__(self)

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(LoadPreset())
        self.addAlgorithm(UpdateEar())
        self.addAlgorithm(SeznamParcelZnotrajObmojaRaziskave())
        self.addAlgorithm(UpdateZkn())
        self.addAlgorithm(DownloadLidar())


    def id(self):
        return 'agis_analiza'

    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.

        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr('AGIS analiza v 0.5')

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        provider_icone = path('icons')/'agis_analiza.png'
        return QIcon(str(provider_icone))
