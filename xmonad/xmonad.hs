--IMPORTS
import XMonad
import Data.Monoid
import System.Exit

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

import XMonad.Util.SpawnOnce
import XMonad.Util.Run
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.DynamicLog
import XMonad.Layout.Spacing
import XMonad.Layout.MultiColumns
import XMonad.Layout.PerWorkspace
import XMonad.Layout.SimpleFloat
import XMonad.Layout.NoBorders

--VARIABLES

myFocusFollowsMouse :: Bool
myClickJustFocuses :: Bool

myTerminal          = "urxvt"
myBrowser           = "brave"
fileManager         = "gvifm"
myBorderWidth       = 3
myModMask           = mod1Mask
myWorkspaces        = ["1", "2", "3", "4", "5", "6"]
myNormalBorderColor  = "#dddddd"
myFocusedBorderColor = "#588FF4"
myFocusFollowsMouse = True 
myClickJustFocuses = False
volume_diff = "5" 

myStartupHook = do
        spawnOnce "nitrogen --restore &"
        spawnOnce "nm-applet &"
        spawnOnce "pamixer --get-volume > ~/.vol &"

myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $
    [
      --MY WINDOWS
      ((mod4Mask, xK_Return), spawn myTerminal)               --terminal                          
    , ((modm, xK_p), spawn "dmenu_run")                       --dmenu
    , ((mod4Mask, xK_b), spawn myBrowser)                     --run the web browser
    , ((mod4Mask, xK_f), spawn fileManager)                   --file Manager
    , ((mod4Mask, xK_g), spawn "nvidia-control-panel")        --nvidia settings

    --VOLUME
    , ((mod4Mask, xK_3), spawn ("vdec"))
    , ((mod4Mask, xK_4), spawn ("vinc"))
    
    --WINDOW MANAGEMENT
    , ((mod4Mask, xK_BackSpace), kill)                        --kill focused window
    , ((modm, xK_space ), sendMessage NextLayout)             --scroll layout algos
    , ((modm, xK_n), refresh)                                 --restore the size
    , ((modm, xK_Tab), windows W.focusDown)                   --focus to the next window
    , ((modm, xK_j), windows W.focusDown)                     --focus to the next window
    , ((modm, xK_k), windows W.focusUp)                       --focus to the previous window
    , ((modm, xK_m), windows W.focusMaster  )                 --focus to master   
    , ((modm, xK_Return), windows W.swapMaster)               --swap with master
    , ((modm .|. shiftMask, xK_j), windows W.swapDown)        --swap with next
    , ((modm .|. shiftMask, xK_k), windows W.swapUp)          --swap with previous
    , ((modm, xK_h), sendMessage Shrink)                      --shrink master
    , ((modm, xK_l), sendMessage Expand)                      --expand master
    , ((modm, xK_t), withFocused $ windows . W.sink)          --push to tiling
    , ((modm, xK_comma), sendMessage (IncMasterN 1))          --increment the number in master
    , ((modm, xK_period), sendMessage (IncMasterN (-1)))      --deincrement the number in master
    , ((modm, xK_b), sendMessage ToggleStruts)                --toggle struts
    
    --XMONAD
    , ((modm .|. shiftMask, xK_q), io (exitWith ExitSuccess)) --quit xmonad
    , ((modm, xK_q), spawn "killall xmobar; xmonad --recompile; xmonad --restart") --restart xmonad
    ]
    ++
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]
    ++

    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    --
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]

myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster)) --set to floating+move
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster)) --raise to the top of the stack
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster)) --set to floating+resize
    ]


myLayout = avoidStruts (tiled ||| multiCol [1] 1 0.01 (-0.5) ||| Full)
  where
     -- default tiling algorithm partitions the screen into two panes
     tiled   = Tall nmaster delta ratio

     -- The default number of windows in the master pane
     nmaster = 1 

     -- Default proportion of screen occupied by master pane
     ratio   = 1/2

     -- Percent of screen to increment by when resizing panes
     delta   = 3/100

full_layout = noBorders Full

gites = onWorkspace "3" full_layout $
        myLayout

defaults = def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = gites,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        logHook            = myLogHook,
        startupHook        = myStartupHook
    }

myManageHook = composeAll []
myEventHook = mempty
myLogHook = return ()

main = do
  xmproc0 <- spawnPipe "xmobar -x 0 /home/mcnuggetsx20/.xmonad/xmobar/xmobar.config"
  xmproc1 <- spawnPipe "trayer --edge top --monitor 1 --distancefrom rigt --distance 265 --height 20 --width 38 --align right --tint 0x000000 --alpha 65 --transparent true --iconspacing 10"
  xmonad $ docks defaults

