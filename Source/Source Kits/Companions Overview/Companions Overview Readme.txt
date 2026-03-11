COMPANIONS OVERVIEW (1.01) by Lav
Released 8/30/11

Taleworlds:   http://forums.taleworlds.com/index.php/topic,182926.0.html
MBRepository: 

###################################################################################################
                                           INSTRUCTIONS
###################################################################################################

INSTALLATION INSTRUCTIONS (with Modmerger):
1) Verify that you have modmerger framework 0.2.5 (last version since Aug 2010) installed.
2) Add the tournament_*.py files to the same directory as your module system *.py files.
3) In "modmerger_options.py" add (under the mods_active section):

   	"companions",      # Lav's Companions Overview (1.01)

4) Follow the rest of the file specific instructions listed below.  Some of these items
   should already be done, but are listed to help catch conflicts.

##############################################################################
#                                MODULE_DIALOGS                              #
##############################################################################

1) In module_dialogs.py add the following directly after "dialogs = [" at the file beginning.

  [anyone, "start", [(eq,"$g_lco_operation",lco_view_character)],"Here you are.","lco_conversation_end",[(change_screen_view_character)]],


2) In module_dialogs.py add the following somewhere towards the end prior to the final "]":

  [anyone, "lco_conversation_end", [(troop_is_hero,"$g_lco_target"),(assign,"$g_lco_operation",lco_run_presentation)], "Nice to know you are not forgetting me!", "close_window", [(change_screen_return)]],
  [anyone, "lco_conversation_end", [(assign,"$g_lco_operation",lco_run_presentation)], "It's a honor to serve you, {sir/my lady}!", "close_window", [(change_screen_return)]],


##############################################################################
#                                 MODULE_TROOPS                              #
##############################################################################
1) In module_troops.py you need to add the following lines towards the end prior to final "]":

  ["companions_overview", "{!}Hidden", "{!}Hidden",tf_hero,0,0,0,[],def_attrib|level(1),wp(100),knows_inventory_management_10,0],
  ["companions_discard", "{!}Hidden", "{!}Hidden",tf_hero,0,0,0,[],def_attrib|level(1),wp(100),knows_inventory_management_10,0],


##############################################################################
#                                 VARIABLES.TXT                              #
##############################################################################
1) Add the following list of global variables at the end of the file:

g_lco_active_hero
g_lco_page
g_lco_operation
g_lco_target
g_lco_include_companions
g_lco_include_lords
g_lco_include_regulars
g_lco_initialized
g_lco_heroes
g_lco_dialog
g_lco_return
g_lco_inc_0
g_lco_inc_1
g_lco_inc_2
g_lco_main_container
g_lco_titles_1
g_lco_titles_2
g_lco_attributes_1
g_lco_attributes_2
g_lco_active_panel


###################################################################################################
                                         END OF INSTRUCTIONS
###################################################################################################

