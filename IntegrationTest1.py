from numpy import outer
import pytest
import cv2
import time
import datetime as datetime

from modules.decklinksrc.decklinkSrcWorker_taxi import DeckLinkSRC
from modules.mergeImageWithTelemetry.mergedData import MergedData
from modules.targetAcquisition.targetAcquisition import TargetAcquisition
from modules.geolocation.geolocation import Geolocation
from modules.timestamp.timestamp import Timestamp
from modules.mergeImageWithTelemetry.mergeImageWithTelemetry import MergeImageWithTelemetry

#@pytest.fixture
def get_image():
    img1 = cv2.imread('frame1.jpg')
    return img1
    # cv2.imshow('img', img1) #JUST TO CHECK IF IMAGE IS TAKEN CORRECTLY
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def test_targetAcquisition_to_geolocation(get_image):
    decklinkSrc = DeckLinkSRC()
    target = TargetAcquisition()
    location = Geolocation()
    #merged = MergeImageWithTelemetry()

    euler = {
        'yaw': 5.0,
        'pitch': 2.0,
        'roll': 0.0
    }
    gps = {
        'longitude': 43.4723,
        'latitude': -80.5449,
        'altitude': 100
    }
    telemetry = {
        'eulerAnglesOfPlane': euler,
        'eulerAnglesOfCamera': euler,
        'gpsCoordinates': gps
    }

    merged = MergedData(get_image, telemetry)

    #merged.telemetryData = merged # array needs to be declared here
    #merged.image = get_image

    target.set_curr_frame(merged)
    check1, coordinates_and_telemetry = target.get_coordinates()

    location.set_constants()
    check2, geo_coordinates = location.run_locator(telemetry, get_image) # put things in here parameter to test? find out 
    # check3, locations = location.run_output(geo_coordinates)        # how to connect both modules through paramters?
    print (check1, coordinates_and_telemetry)
    print (check2, geo_coordinates)

    # assert check1 == True and coordinates_and_telemetry != None
    # assert check2 == True and geo_coordinates != None
    # assert check3 == True and locations != None

test = get_image()
test_targetAcquisition_to_geolocation(test)