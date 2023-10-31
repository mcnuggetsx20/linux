
command = f'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @{config.RES_CUSTOM} +0+0 {{ViewPortIn={config.RES_CUSTOM}, ViewPortOut={[config.SCALE_TO]}+{offset[0]}+{offset[1]}, ForceCompositionPipeline=Off, ForceFullCompositionPipeline=Off}}"'

command2 = 'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @3440x1440 +0+0 {ViewPortIn=3440x1440, ViewPortOut=3440x1440+0+0, ForceCompositionPipeline=On, ForceFullCompositionPipeline=On}"'

from subprocess import Popen

Popen(command, shell=True)
