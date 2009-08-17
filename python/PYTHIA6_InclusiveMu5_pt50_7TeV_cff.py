import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *

source = cms.Source("EmptySource")
from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(0.0246),
    crossSection = cms.untracked.double(7290000.),
    comEnergy = cms.double(7000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=1           ! User defined processes', 
            'CKIN(3)=50.      ! minimum pt hat for hard interactions',
            'MSTJ(22)=4       ! Decay unstable particles inside a cylinder',
            'PARJ(73)=2000.   ! max. radius for MSTJ(22)=4',
            'PARJ(74)=4000.   ! max. Z for MSTJ(22)=4',
            'MDCY(C130,1)=1   ! decay k0-longs',
            'MDCY(C211,1)=1   ! decay pions',
            'MDCY(C321,1)=1   ! decay kaons'),

        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
                           MinPt = cms.untracked.vdouble(5.,5.),
                           MinEta = cms.untracked.vdouble(-2.5,-2.5),
                           MaxEta = cms.untracked.vdouble(2.5,2.5),
                           ParticleID = cms.untracked.vint32(13,-13),
                           Status = cms.untracked.vint32(1,1),
                           # Decay cuts are in mm
                           MaxDecayRadius = cms.untracked.vdouble(2000.,2000.),
                           MinDecayZ = cms.untracked.vdouble(-4000.,-4000.),
                           MaxDecayZ = cms.untracked.vdouble(4000.,4000.)
)


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.6 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_InclusiveMu5_pt50_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6-MinBias at 7TeV, pthat>50, with INCLUSIVE muon preselection (pt(mu) > 5)')
)

ProductionFilterSequence = cms.Sequence(generator*mugenfilter)
