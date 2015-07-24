

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias/RunIIWinter15GS_UE_08052015_Run2015B/150723_121340/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_0000.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias1/RunIIWinter15GS_UE_08052015_Run2015B_1/150723_121327/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_1111.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias2/RunIIWinter15GS_UE_08052015_Run2015B_2/150723_122717/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_2222.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias3/RunIIWinter15GS_UE_08052015_Run2015B_3/150723_122732/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_3333.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias4/RunIIWinter15GS_UE_08052015_Run2015B_4/150723_122618/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_4444.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias5/RunIIWinter15GS_UE_08052015_Run2015B_5/150723_122635/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_5555.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias6/RunIIWinter15GS_UE_08052015_Run2015B_6/150723_122649/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_6666.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias7/RunIIWinter15GS_UE_08052015_Run2015B_7/150723_122704/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_7777.root
    fi
done  

cp -v /scratch/osg/rankdw/Run2015B_8DataSets/store/user/dciangot/ZeroBias8/RunIIWinter15GS_UE_08052015_Run2015B_8/150723_122604/0000/*.root /scratch/osg/rankdw/Run2015B_8DataSetsMerged

for f in $( ls /scratch/osg/rankdw/Run2015B_8DataSetsMerged/*.root); do
    if [ ${#f} -lt 60 ]; then
        mv "$f" "${f/.root}"_8888.root
    fi
done  

