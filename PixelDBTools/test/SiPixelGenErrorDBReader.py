import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("SiPixelGenErrorDBReader")

process.load("CondCore.DBCommon.CondDBSetup_cfi") # needed for custom tags

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
# process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.load("Configuration.StandardSequences.GeometryIdeal_cff")
process.load("Configuration.Geometry.GeometryDB_cff")

process.source = cms.Source("EmptySource",
#    firstRun = cms.untracked.uint32(1), #  
#    firstRun = cms.untracked.uint32(210000), #  
#    firstRun = cms.untracked.uint32(238000), #  iov1 
#    firstRun = cms.untracked.uint32(239000), # iov2 in offline  
    firstRun = cms.untracked.uint32(253000), # iov2 in prompt
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

#testGlobalTag = False
#if testGlobalTag :
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
# from Configuration.AlCa.GlobalTag import GlobalTag
# works with condDB and condDBv2
# process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v0', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_75_V1A', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'FT_R_74_V15B', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
# for local sqlite files

testTag = True
if testTag :
#else:
#    process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    process.DBReader = cms.ESSource("PoolDBESSource",
       process.CondDBSetup,
       toGet = cms.VPSet(
         cms.PSet(
           record = cms.string('SiPixelGenErrorDBObjectRcd'),
           tag = cms.string('SiPixelGenErrorDBObject_38T_v1_offline')
#           tag = cms.string('SiPixelGenErrorDBObject_38T_v2_express')
#           tag = cms.string('SiPixelGenErrorDBObject_38T_2015_v1_hltvalidation')
#           tag = cms.string('SiPixelGenErrorDBObject_0T_2015_v1_hltvalidation')
#           tag = cms.string('SiPixelGenErrorDBObject38Tv1')
#           tag = cms.string('SiPixelGenErrorDBObject38Tv3')
         )),
        #timetype = cms.string('runnumber'),
        #connect = cms.string('sqlite_file:../../../../../DB/siPixelGenErrors38T_v1_mc.db')
        #connect = cms.string('sqlite_file:../../../../../DB/siPixelGenErrors38T_2012_IOV7_v1.db')
        #connect = cms.string('sqlite_file:../../../../../DB/siPixelGenErrors38T_IOV8a.db')
        #connect = cms.string('frontier://FrontierProd/CMS_COND_31X_PIXEL')
        #connect = cms.string('frontier://FrontierProd/CMS_COND_PIXEL_000')
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
        #connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
        #connect = cms.string('frontier://FrontierPrep/CMS_COND_PIXEL')

    )
    #process.PoolDBESSource.DBParameters.authenticationPath='.'
    #process.PoolDBESSource.DBParameters.messageLevel=0

    process.es_prefer_DBReader = cms.ESPrefer("PoolDBESSource","DBReader")

#end if

process.reader = cms.EDAnalyzer("SiPixelGenErrorDBReader",
#                     siPixelGenErrorCalibrationLocation = cms.string("./"),
                     siPixelGenErrorCalibrationLocation = cms.string(""),
#Change to True if you would like a more detailed error output
#wantDetailedOutput = False
#Change to True if you would like to output the full GenError database object
#wantFullOutput = False
                     wantDetailedGenErrorDBErrorOutput = cms.bool(True),
                     wantFullGenErrorDBOutput = cms.bool(False)
                 )

process.p = cms.Path(process.reader)






