from module_troops_part1 import *
from module_troops_part2 import *

troops = troops_part1 + troops_part2


####Troop upgrade declarations
## Floris: Multiple troop trees
###Mercenaries
##Native troop tree
#Tier 1-2
upgrade(troops,"mercenary_n_townsman","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_farmer","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra1","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra2","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra3","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra4","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra5","mercenary_n_spiessknecht")
#Tier 2-3
upgrade2(troops,"mercenary_n_spiessknecht","mercenary_n_page","mercenary_n_armbrust_soldner")
#Tier 3-4
upgrade2(troops,"mercenary_n_page","mercenary_n_soldner","mercenary_n_ritter")
#Tier 4-5
upgrade(troops,"mercenary_n_soldner","mercenary_n_komtur")
upgrade(troops,"mercenary_n_ritter","mercenary_n_komtur_ritter")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"mercenary_r_townsman","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_farmer","mercenary_r_spiessknecht","mercenary_r_armbruster")
upgrade2(troops,"mercenary_r_extra1","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra2","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra3","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra4","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra5","mercenary_r_edelknecht","mercenary_r_spiessknecht")
#Tier 2-3
upgrade(troops,"mercenary_r_edelknecht","mercenary_r_burger")
upgrade2(troops,"mercenary_r_spiessknecht","mercenary_r_halberdier","mercenary_r_page")
upgrade(troops,"mercenary_r_armbruster","mercenary_r_armbrust_miliz")
#Tier 3-4
upgrade(troops,"mercenary_r_burger","mercenary_r_brabanzon")
upgrade(troops,"mercenary_r_halberdier","mercenary_r_reichslandser")
upgrade(troops,"mercenary_r_page","mercenary_r_ritter")
upgrade(troops,"mercenary_r_armbrust_miliz","mercenary_r_armbrust_soldner")
#Tier 4-5
upgrade(troops,"mercenary_r_brabanzon","mercenary_r_doppelsoldner")
upgrade(troops,"mercenary_r_reichslandser","mercenary_r_burgmann")
upgrade(troops,"mercenary_r_ritter","mercenary_r_komtur_ritter")
upgrade(troops,"mercenary_r_armbrust_soldner","mercenary_r_armbrust_komtur")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"mercenary_e_townsman","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_farmer","mercenary_e_spiessknecht","mercenary_e_armbruster")
upgrade2(troops,"mercenary_e_extra1","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra2","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra3","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra4","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra5","mercenary_e_miliz","mercenary_e_edelknecht")
#Tier 2-3
upgrade2(troops,"mercenary_e_miliz","mercenary_e_brabanzon","mercenary_e_burger")
upgrade2(troops,"mercenary_e_edelknecht","mercenary_e_volksheer","mercenary_e_halberdier")
upgrade2(troops,"mercenary_e_spiessknecht","mercenary_e_halberdier","mercenary_e_page")
upgrade2(troops,"mercenary_e_armbruster","mercenary_e_armbrust_soldner","mercenary_e_armbrust_miliz")
#Tier 3-4
upgrade(troops,"mercenary_e_brabanzon","mercenary_e_ritterbroeder")
upgrade(troops,"mercenary_e_volksheer","mercenary_e_soldner")
upgrade(troops,"mercenary_e_halberdier","mercenary_e_reichslandser")
upgrade(troops,"mercenary_e_page","mercenary_e_ritter")
upgrade(troops,"mercenary_e_armbrust_soldner","mercenary_e_armbrust_komtur")
#Tier 4-5
upgrade(troops,"mercenary_e_ritterbroeder","mercenary_e_doppelsoldner")
upgrade(troops,"mercenary_e_soldner","mercenary_e_komtur")
upgrade(troops,"mercenary_e_reichslandser","mercenary_e_burgmann")
upgrade2(troops,"mercenary_e_ritter","mercenary_e_komtur_ritter","mercenary_e_kreuzritter")
#Tier 5-6
upgrade(troops,"mercenary_e_komtur","mercenary_e_grosskomtur")
upgrade(troops,"mercenary_e_burgmann","mercenary_e_landsknecht")
upgrade(troops,"mercenary_e_komtur_ritter","mercenary_e_hochmeister")
##

###Swadia
##Native troop tree
#Tier 1-2
upgrade(troops,"swadian_n_peasant","swadian_n_militia")
upgrade(troops,"swadian_n_extra1","swadian_n_militia")
upgrade(troops,"swadian_n_extra2","swadian_n_militia")
upgrade(troops,"swadian_n_extra3","swadian_n_militia")
upgrade(troops,"swadian_n_extra4","swadian_n_militia")
upgrade(troops,"swadian_n_extra5","swadian_n_militia")
#Tier 2-3
upgrade2(troops,"swadian_n_militia","swadian_n_page","swadian_n_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_n_page","swadian_n_ecuyer","swadian_n_foot_soldier")
upgrade(troops,"swadian_n_archer_militia","swadian_n_trained_archer")
#Tier 4-5
upgrade(troops,"swadian_n_ecuyer","swadian_n_chevalier")
upgrade(troops,"swadian_n_foot_soldier","swadian_n_infantry")
upgrade(troops,"swadian_n_trained_archer","swadian_n_selfbow_archer")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"swadian_r_peasant","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra1","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra2","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra3","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra4","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra5","swadian_r_militia","swadian_r_peasant_archer")
#Tier 2-3
upgrade(troops,"swadian_r_militia","swadian_r_page")
upgrade2(troops,"swadian_r_peasant_archer","swadian_r_sergeant_at_arms","swadian_r_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_r_page","swadian_r_hobilar","swadian_r_ecuyer")
upgrade2(troops,"swadian_r_sergeant_at_arms","swadian_r_piquier","swadian_r_foot_soldier")
upgrade(troops,"swadian_r_archer_militia","swadian_r_trained_archer")
#Tier 4-5
upgrade(troops,"swadian_r_ecuyer","swadian_r_chevalier")
upgrade(troops,"swadian_r_foot_soldier","swadian_r_infantry")
upgrade(troops,"swadian_r_trained_archer","swadian_r_selfbow_archer")
#Tier 5-6
upgrade(troops,"swadian_r_chevalier","swadian_r_chevalier_banneret")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"swadian_e_peasant","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra1","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra2","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra3","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra4","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra5","swadian_e_militia","swadian_e_peasant_archer")
#Tier 2-3
upgrade(troops,"swadian_e_militia","swadian_e_vougier")
upgrade(troops,"swadian_e_peasant_archer","swadian_e_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_e_vougier","swadian_e_foot_soldier","swadian_e_hobilar")
upgrade2(troops,"swadian_e_page","swadian_e_ecuyer","swadian_e_hobilar")
upgrade(troops,"swadian_e_archer_militia","swadian_e_trained_archer")
#Tier 4-5
upgrade2(troops,"swadian_e_ecuyer","swadian_e_chevalier","swadian_e_man_at_arms")
upgrade(troops,"swadian_e_foot_soldier","swadian_e_infantry")
upgrade(troops,"swadian_e_hobilar","swadian_e_man_at_arms")
upgrade(troops,"swadian_e_trained_archer","swadian_e_selfbow_archer")
#Tier 5-6
upgrade2(troops,"swadian_e_chevalier","swadian_e_chevalier_banneret","swadian_e_lancer")
upgrade(troops,"swadian_e_infantry","swadian_e_sergeant")
upgrade(troops,"swadian_e_man_at_arms","swadian_e_lancer")
upgrade(troops,"swadian_e_selfbow_archer","swadian_e_longbowman")
#Tier 6-7
upgrade(troops,"swadian_e_chevalier_banneret","swadian_e_baron_mineures")
upgrade(troops,"swadian_e_longbowman","swadian_e_retinue_longbowman")
##

###Vaegir
##Native troop tree
#Tier 1-2
upgrade(troops,"vaegir_n_kholop","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra1","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra2","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra3","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra4","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra5","vaegir_n_otrok")
#Tier 2-3
upgrade2(troops,"vaegir_n_otrok","vaegir_n_kazak","vaegir_n_kmet")
#Tier 3-4
upgrade2(troops,"vaegir_n_kazak","vaegir_n_yesaul","vaegir_n_plastun")
upgrade(troops,"vaegir_n_kmet","vaegir_n_zalstrelshik")
#Tier 4-5
upgrade(troops,"vaegir_n_yesaul","vaegir_n_pansirniy_kazan")
upgrade(troops,"vaegir_n_plastun","vaegir_n_druzhinnik_veteran")
upgrade(troops,"vaegir_n_zalstrelshik","vaegir_n_luchnik")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"vaegir_r_kholop","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra1","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra2","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra3","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra4","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra5","vaegir_r_otrok","vaegir_r_pasynok")
#Tier 2-3
upgrade2(troops,"vaegir_r_otrok","vaegir_r_kazak","vaegir_r_kmet")
upgrade2(troops,"vaegir_r_pasynok","vaegir_r_kmet","vaegir_r_grid")
#Tier 3-4
upgrade(troops,"vaegir_r_kazak","vaegir_r_yesaul")
upgrade2(troops,"vaegir_r_kmet","vaegir_r_ratnik","vaegir_r_zalstrelshik")
upgrade2(troops,"vaegir_r_grid","vaegir_r_plastun","vaegir_r_mladshiy_druzhinnik")
#Tier 4-5
upgrade(troops,"vaegir_r_yesaul","vaegir_r_ataman")
upgrade(troops,"vaegir_r_zalstrelshik","vaegir_r_luchnik")
upgrade(troops,"vaegir_r_mladshiy_druzhinnik","vaegir_r_druzhinnik_veteran")
#Tier 5-6
upgrade(troops,"vaegir_r_luchnik","vaegir_r_metkiy_luchnik")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"vaegir_e_kholop","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra1","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra2","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra3","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra4","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra5","vaegir_e_otrok","vaegir_e_pasynok")
#Tier 2-3
upgrade2(troops,"vaegir_e_otrok","vaegir_e_kazak","vaegir_e_kmet")
upgrade2(troops,"vaegir_e_pasynok","vaegir_e_kmet","vaegir_e_grid")
#Tier 3-4
upgrade2(troops,"vaegir_e_kazak","vaegir_e_yesaul","vaegir_e_plastun")
upgrade2(troops,"vaegir_e_kmet","vaegir_e_ratnik","vaegir_e_zalstrelshik")
upgrade2(troops,"vaegir_e_grid","vaegir_e_mladshiy_druzhinnik","vaegir_e_poztoma_druzhinaik")
#Tier 4-5
upgrade2(troops,"vaegir_e_yesaul","vaegir_e_ataman","vaegir_e_pansirniy_kazan")
upgrade2(troops,"vaegir_e_ratnik","vaegir_e_posadnik","vaegir_e_golova")
upgrade(troops,"vaegir_e_zalstrelshik","vaegir_e_luchnik")
upgrade(troops,"vaegir_e_mladshiy_druzhinnik","vaegir_e_druzhinnik")
upgrade(troops,"vaegir_e_poztoma_druzhinaik","vaegir_e_druzhinnik_veteran")
#Tier 5-6
upgrade(troops,"vaegir_e_ataman","vaegir_e_legkoy_vityas")
upgrade(troops,"vaegir_e_pansirniy_kazan","vaegir_e_vityas")
upgrade(troops,"vaegir_e_posadnik","vaegir_e_voevoda")
upgrade(troops,"vaegir_e_luchnik","vaegir_e_metkiy_luchnik")
upgrade(troops,"vaegir_e_druzhinnik","vaegir_e_elitniy_druzhinnik")
#Tier 6-7
upgrade(troops,"vaegir_e_vityas","vaegir_e_bogatyr")
upgrade(troops,"vaegir_e_metkiy_luchnik","vaegir_e_sokoliniy_glaz")
##

###Khergit
##Native troop tree
#Tier 1-2
upgrade(troops,"khergit_n_tariachin","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra1","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra2","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra3","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra4","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra5","khergit_n_qarbughaci")
#Tier 2-3
upgrade(troops,"khergit_n_qarbughaci","khergit_n_morici")
#Tier 3-4
upgrade2(troops,"khergit_n_morici","khergit_n_kipchak","khergit_n_qubuci")
#Tier 4-5
upgrade(troops,"khergit_n_qubuci","khergit_n_borjigin")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"khergit_r_tariachin","khergit_r_tsereg","khergit_r_qarbughaci")
upgrade2(troops,"khergit_r_extra1","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra2","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra3","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra4","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra5","khergit_r_qarbughaci","khergit_r_tsereg")
#Tier 2-3
upgrade(troops,"khergit_r_tsereg","khergit_r_asud")
upgrade2(troops,"khergit_r_qarbughaci","khergit_r_morici","khergit_r_abaci")
#Tier 3-4
upgrade2(troops,"khergit_r_morici","khergit_r_quaqli","khergit_r_kipchak")
upgrade2(troops,"khergit_r_abaci","khergit_r_teriguci","khergit_r_qubuci")
upgrade(troops,"khergit_r_asud","khergit_r_aqala_asud")
#Tier 4-5
upgrade(troops,"khergit_r_quaqli","khergit_r_khevtuul")
upgrade(troops,"khergit_r_teriguci","khergit_r_aqala_teriguci")
upgrade(troops,"khergit_r_qubuci","khergit_r_borjigin")
#Tier 5-6
upgrade(troops,"khergit_r_aqala_teriguci","khergit_r_keshig")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"khergit_e_tariachin","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra1","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra2","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra3","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra4","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra5","khergit_e_tsereg","khergit_e_qarbughaci")
#Tier 2-3
upgrade2(troops,"khergit_e_tsereg","khergit_e_morici","khergit_e_asud")
upgrade2(troops,"khergit_e_qarbughaci","khergit_e_surcin","khergit_e_abaci")
#Tier 3-4
upgrade2(troops,"khergit_e_morici","khergit_e_kipchak","khergit_e_quaqli")
upgrade(troops,"khergit_e_asud","khergit_e_aqala_asud")
upgrade(troops,"khergit_e_surcin","khergit_e_aqala_surcin")
upgrade2(troops,"khergit_e_abaci","khergit_e_teriguci","khergit_e_qubuci")
#Tier 4-5
upgrade(troops,"khergit_e_kipchak","khergit_e_torguu")
upgrade(troops,"khergit_e_quaqli","khergit_e_khevtuul")
upgrade(troops,"khergit_e_aqala_asud","khergit_e_yabagharu_morici")
upgrade2(troops,"khergit_e_aqala_surcin","khergit_e_numyn_ad","khergit_e_numici")
upgrade(troops,"khergit_e_teriguci","khergit_e_aqala_teriguci")
upgrade(troops,"khergit_e_qubuci","khergit_e_borjigin")
#Tier 5-6
upgrade(troops,"khergit_e_torguu","khergit_e_khorchen")
upgrade(troops,"khergit_e_khevtuul","khergit_e_keshig")
upgrade(troops,"khergit_e_numici","khergit_e_kharvaach")
upgrade(troops,"khergit_e_aqala_teriguci","khergit_e_jurtchi")
upgrade(troops,"khergit_e_borjigin","khergit_e_aqata_borjigin")
#Tier 6-7
upgrade(troops,"khergit_e_khorchen","khergit_e_cherbi")
upgrade(troops,"khergit_e_aqata_borjigin","khergit_e_mandugai")
##

###Nord
##Native troop tree
#Tier 1-2
upgrade2(troops,"nord_n_bondi","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra1","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra2","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra3","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra4","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra5","nord_n_huskarl","nord_n_gesith")
#Tier 2-3
upgrade(troops,"nord_n_huskarl","nord_n_gridman")
upgrade(troops,"nord_n_gesith","nord_n_bogmadur")
#Tier 3-4
upgrade(troops,"nord_n_gridman","nord_n_vigamadr")
upgrade(troops,"nord_n_bogmadur","nord_n_bogsveigir")
#Tier 4-5
upgrade(troops,"nord_n_vigamadr","nord_n_skjadsveinn")
#Tier 5-6
upgrade(troops,"nord_n_skjadsveinn","nord_n_husbondi")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"nord_r_bondi","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra1","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra2","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra3","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra4","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra5","nord_r_berserkr","nord_r_huskarl")
#Tier 2-3
upgrade(troops,"nord_r_berserkr","nord_r_kertilsveinr")
upgrade2(troops,"nord_r_huskarl","nord_r_gesith","nord_r_gridman")
#Tier 3-4
upgrade(troops,"nord_r_kertilsveinr","nord_r_vikingr")
upgrade2(troops,"nord_r_gesith","nord_r_bogsveigir","nord_r_hermadur")
upgrade2(troops,"nord_r_gridman","nord_r_innaesmaen","nord_r_vigamadr")
#Tier 4-5
upgrade(troops,"nord_r_hermadur","nord_r_heahgerefa")
upgrade(troops,"nord_r_vigamadr","nord_r_skjadsveinn")
#Tier 5-6
upgrade(troops,"nord_r_skjadsveinn","nord_r_husbondi")
####Expanded troop tree
#Tier 1-2  (Recruit -> Footman)
upgrade(troops,"nord_e_recruit","nord_e_footman")
upgrade(troops,"nord_e_extra1","nord_e_footman")
upgrade(troops,"nord_e_extra2","nord_e_footman")
upgrade(troops,"nord_e_extra3","nord_e_footman")
upgrade(troops,"nord_e_extra4","nord_e_footman")
upgrade(troops,"nord_e_extra5","nord_e_footman")
#Tier 2-3  (Footman -> A3 Huntsman OR I3 Trained Footman)
upgrade2(troops,"nord_e_footman","nord_e_huntsman","nord_e_trained_footman")
#Tier 3-4  (Huntsman -> A4 Skirmisher OR A4 Archer)
upgrade2(troops,"nord_e_huntsman","nord_e_skirmisher","nord_e_archer")
#           (Trained Footman -> I4 Axeman OR C4 Scout; Dreng -> I4 Warrior OR C4 Scout)
upgrade2(troops,"nord_e_trained_footman","nord_e_axeman","nord_e_scout")
upgrade2(troops,"nord_e_dreng","nord_e_warrior","nord_e_scout")
#Tier 4-5  (Skirmisher -> A5 Vet.Skirmisher; Archer -> A5 Vet.Archer)
upgrade(troops,"nord_e_skirmisher","nord_e_veteran_skirmisher")
upgrade(troops,"nord_e_archer","nord_e_veteran_archer")
#           (Axeman -> I5 Vikingr; Warrior -> I5 Champion OR I5 Vikingr)
upgrade(troops,"nord_e_axeman","nord_e_vikingr")
upgrade2(troops,"nord_e_warrior","nord_e_champion","nord_e_vikingr")
#Tier 5-6  (Vet.Skirmisher -> A6 Javelinier)
upgrade(troops,"nord_e_veteran_skirmisher","nord_e_javelinier")
#           (Champion -> I6 Marauder OR I6 Huskarl; Vikingr -> I6 Marauder)
upgrade2(troops,"nord_e_champion","nord_e_marauder","nord_e_huskarl")
upgrade(troops,"nord_e_vikingr","nord_e_marauder")
#Tier 6-7  (Marauder -> I7 Berserkr; Huskarl -> I7 Berserkr OR I7 Elite Huskarl)
upgrade(troops,"nord_e_marauder","nord_e_berserkr")
upgrade2(troops,"nord_e_huskarl","nord_e_berserkr","nord_e_elite_huskarl")
##

###Rhodok
##Native troop tree
#Tier 1-2
upgrade2(troops,"rhodok_n_cittadino","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra1","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra2","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra3","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra4","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra5","rhodok_n_novizio","rhodok_n_recluta_balestriere")
#Tier 2-3
upgrade(troops,"rhodok_n_novizio","rhodok_n_milizia")
upgrade(troops,"rhodok_n_recluta_balestriere","rhodok_n_milizia_balestriere")
#Tier 3-4
upgrade(troops,"rhodok_n_milizia","rhodok_n_fante")
upgrade(troops,"rhodok_n_milizia_balestriere","rhodok_n_balestriere")
#Tier 4-5
upgrade(troops,"rhodok_n_fante","rhodok_n_veterano")
upgrade(troops,"rhodok_n_balestriere","rhodok_n_balestriere_veterano")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"rhodok_r_cittadino","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra1","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra2","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra3","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra4","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra5","rhodok_r_novizio","rhodok_r_recluta")
#Tier 2-3
upgrade(troops,"rhodok_r_novizio","rhodok_r_lanciere_a_cavallo")
upgrade2(troops,"rhodok_r_recluta","rhodok_r_recluta_balestriere","rhodok_r_lanciere")
#Tier 3-4
upgrade(troops,"rhodok_r_lanciere_a_cavallo","rhodok_r_lanza_spezzata")
upgrade2(troops,"rhodok_r_recluta_balestriere","rhodok_r_balestriere","rhodok_r_balestriere_leggero")
upgrade2(troops,"rhodok_r_lanciere","rhodok_r_lanciere_veterano","rhodok_r_fante")
#Tier 4-5
upgrade(troops,"rhodok_r_balestriere_leggero","rhodok_r_balestriere_d_assedio")
upgrade(troops,"rhodok_r_lanciere_veterano","rhodok_r_picchiere_veterano")
#Tier 5-6
upgrade(troops,"rhodok_r_balestriere_d_assedio","rhodok_r_capitano_d_assedio")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"rhodok_e_cittadino","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra1","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra2","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra3","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra4","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra5","rhodok_e_novizio","rhodok_e_recluta")
#Tier 2-3
upgrade2(troops,"rhodok_e_novizio","rhodok_e_milizia","rhodok_e_milizia_balestriere")
upgrade2(troops,"rhodok_e_recluta","rhodok_e_recluta_balestriere","rhodok_e_lanciere")
#Tier 3-4
upgrade(troops,"rhodok_e_milizia","rhodok_e_fante")
upgrade2(troops,"rhodok_e_milizia_balestriere","rhodok_e_fante","rhodok_e_balestriere")
upgrade2(troops,"rhodok_e_recluta_balestriere","rhodok_e_balestriere","rhodok_e_balestriere_leggero")
upgrade2(troops,"rhodok_e_lanciere","rhodok_e_lanciere_veterano","rhodok_e_lanciere_a_cavallo")
#Tier 4-5
#upgrade(troops,"rhodok_e_provisionato","rhodok_e_guardia")
upgrade(troops,"rhodok_e_fante","rhodok_e_veterano")
upgrade(troops,"rhodok_e_balestriere","rhodok_e_balestriere_d_assedio")
upgrade(troops,"rhodok_e_balestriere_leggero","rhodok_e_balestriere_a_cavallo")
upgrade(troops,"rhodok_e_lanciere_veterano","rhodok_e_picchiere_veterano")
upgrade(troops,"rhodok_e_lanciere_a_cavallo","rhodok_e_lanza_spezzata")
#Tier 5-6
#upgrade(troops,"rhodok_e_guardia","rhodok_e_guardia_ducale")
upgrade(troops,"rhodok_e_veterano","rhodok_e_capitano_di_ventura")
upgrade(troops,"rhodok_e_balestriere_d_assedio","rhodok_e_capitano_d_assedio")
upgrade(troops,"rhodok_e_picchiere_veterano","rhodok_e_picchiere_fiammingo")
#Tier 6-7
upgrade(troops,"rhodok_e_capitano_d_assedio","rhodok_e_condottiero_d_assedio")
upgrade(troops,"rhodok_e_picchiere_fiammingo","rhodok_e_condottiero")
##

###Sarranid
##Native troop tree
#Tier 1-2
upgrade(troops,"sarranid_n_millet","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra1","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra2","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra3","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra4","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra5","sarranid_n_ajam")
#Tier 2-3
upgrade2(troops,"sarranid_n_ajam","sarranid_n_cemaat","sarranid_n_jebelus")
#Tier 3-4
upgrade2(troops,"sarranid_n_cemaat","sarranid_n_yerliyya","sarranid_n_timariot")
upgrade(troops,"sarranid_n_jebelus","sarranid_n_garip")
#Tier 4-5
upgrade(troops,"sarranid_n_yerliyya","sarranid_n_yeniceri")
upgrade(troops,"sarranid_n_timariot","sarranid_n_kapikula")
upgrade(troops,"sarranid_n_garip","sarranid_n_uluteci")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"sarranid_r_millet","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra1","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra2","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra3","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra4","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra5","sarranid_r_ajam","sarranid_r_oglan")
#Tier 2-3
upgrade2(troops,"sarranid_r_ajam","sarranid_r_azab","sarranid_r_cemaat")
upgrade(troops,"sarranid_r_oglan","sarranid_r_jebelus")
#Tier 3-4
upgrade2(troops,"sarranid_r_azab","sarranid_r_kapikulu_savari","sarranid_r_timariot")
upgrade(troops,"sarranid_r_cemaat","sarranid_r_al_haqa")
upgrade2(troops,"sarranid_r_jebelus","sarranid_r_garip","sarranid_r_badw")
#Tier 4-5
upgrade(troops,"sarranid_r_timariot","sarranid_r_kapikula")
upgrade(troops,"sarranid_r_al_haqa","sarranid_r_yerliyya")
upgrade(troops,"sarranid_r_garip","sarranid_r_uluteci")
#Tier 5-6
upgrade(troops,"sarranid_r_yerliyya","sarranid_r_yeniceri")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"sarranid_e_millet","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra1","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra2","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra3","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra4","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra5","sarranid_e_ajam","sarranid_e_oglan")
#Tier 2-3
upgrade2(troops,"sarranid_e_ajam","sarranid_e_azab","sarranid_e_cemaat")
upgrade2(troops,"sarranid_e_oglan","sarranid_e_jebelus","sarranid_e_ghulam")
#Tier 3-4
upgrade2(troops,"sarranid_e_azab","sarranid_e_al_haqa","sarranid_e_timariot")
upgrade2(troops,"sarranid_e_cemaat","sarranid_e_yerliyya","sarranid_e_kapikulu_savari")
upgrade2(troops,"sarranid_e_jebelus","sarranid_e_garip","sarranid_e_badw")
upgrade2(troops,"sarranid_e_ghulam","sarranid_e_serdengecti","sarranid_e_tabardariyya")
#Tier 4-5
upgrade(troops,"sarranid_e_timariot","sarranid_e_kapikula")
upgrade(troops,"sarranid_e_yerliyya","sarranid_e_yeniceri")
upgrade(troops,"sarranid_e_kapikulu_savari","sarranid_e_beylik")
upgrade(troops,"sarranid_e_garip","sarranid_e_uluteci")
upgrade(troops,"sarranid_e_badw","sarranid_e_akinci")
upgrade(troops,"sarranid_e_serdengecti","sarranid_e_terkes_serdengecti")
#Tier 5-6
upgrade2(troops,"sarranid_e_kapikula","sarranid_e_qilich_arslan","sarranid_e_memluk")
upgrade(troops,"sarranid_e_beylik","sarranid_e_sekban")
upgrade(troops,"sarranid_e_uluteci","sarranid_e_silahtar")
upgrade(troops,"sarranid_e_akinci","sarranid_e_sipahi")
#Tier 6-7
upgrade(troops,"sarranid_e_memluk","sarranid_e_hasham")
upgrade(troops,"sarranid_e_sipahi","sarranid_e_iqta_dar")
##
##STAT Upgrades
upgrade2(troops, "skill_monk", "skill_priest", "skill_surgeon")
upgrade(troops, "skill_priest", "skill_bishop")
###Bandits
##Native troop tree
#Looters
upgrade2(troops,"bandit_n_looter","bandit_n_mountain", "bandit_n_forest")
upgrade2(troops,"bandit_n_bandit","bandit_n_brigand","mercenary_n_soldner")
#Normal Bandits
upgrade(troops,"bandit_n_mountain","rhodok_n_cittadino")
upgrade(troops,"bandit_n_forest","swadian_n_peasant")
upgrade(troops,"bandit_n_sea_raider","nord_n_bondi")
upgrade(troops,"bandit_n_steppe","khergit_n_tariachin")
upgrade(troops,"bandit_n_taiga","vaegir_n_kholop")
upgrade(troops,"bandit_n_desert","sarranid_n_millet")
##Manhunters
upgrade(troops,"bandit_n_manhunter","bandit_n_slave_driver")
upgrade(troops,"bandit_n_slave_driver","bandit_n_slave_hunter")
upgrade(troops,"bandit_n_slave_hunter","bandit_n_slave_crusher")
upgrade(troops,"bandit_n_slave_crusher","bandit_n_slaver_chief")
##Reworked troop tree
#Looters
upgrade2(troops,"bandit_r_looter","bandit_r_bandit", "mercenary_r_edelknecht")
upgrade2(troops,"bandit_r_bandit","bandit_r_brigand","mercenary_r_halberdier")
upgrade2(troops,"bandit_r_brigand","mercenary_r_ritter","mercenary_r_reichslandser")
#Normal Bandits
upgrade2(troops,"bandit_r_mountain","rhodok_r_lanciere","rhodok_r_recluta_balestriere")
upgrade2(troops,"bandit_r_forest","swadian_r_trained_archer","swadian_r_foot_soldier")
upgrade2(troops,"bandit_r_sea_raider","nord_r_vigamadr","nord_r_vikingr")
upgrade2(troops,"bandit_r_steppe","khergit_r_kipchak","khergit_r_qubuci")
upgrade2(troops,"bandit_r_taiga","vaegir_r_yesaul","vaegir_r_zalstrelshik")
upgrade2(troops,"bandit_r_desert","sarranid_r_timariot","sarranid_r_badw")
##Manhunters
upgrade(troops,"bandit_r_manhunter","bandit_r_slave_driver")
upgrade(troops,"bandit_r_slave_driver","bandit_r_slave_hunter")
upgrade(troops,"bandit_r_slave_hunter","bandit_r_slave_crusher")
upgrade(troops,"bandit_r_slave_crusher","bandit_r_slaver_chief")
##Expanded troop tree
#Looters
upgrade2(troops,"bandit_e_looter","bandit_e_bandit", "mercenary_e_edelknecht")
upgrade2(troops,"bandit_e_bandit","bandit_e_brigand","mercenary_e_halberdier")
upgrade2(troops,"bandit_e_brigand","mercenary_e_ritter","mercenary_e_reichslandser")
#Normal Bandits
upgrade2(troops,"bandit_e_mountain","rhodok_e_milizia","rhodok_e_recluta_balestriere")
upgrade2(troops,"bandit_e_forest","swadian_e_trained_archer","swadian_e_foot_soldier")
upgrade2(troops,"bandit_e_sea_raider","nord_e_warrior","nord_e_axeman")
upgrade2(troops,"bandit_e_steppe","khergit_e_kipchak","khergit_e_qubuci")
upgrade2(troops,"bandit_e_taiga","vaegir_e_yesaul","vaegir_e_zalstrelshik")
upgrade2(troops,"bandit_e_desert","sarranid_e_timariot","sarranid_e_badw")
##Manhunters
upgrade(troops,"bandit_e_manhunter","bandit_e_slave_driver")
upgrade(troops,"bandit_e_slave_driver","bandit_e_slave_hunter")
upgrade(troops,"bandit_e_slave_hunter","bandit_e_slave_crusher")
upgrade(troops,"bandit_e_slave_crusher","bandit_e_slaver_chief")
##



###Women
##Native troop tree
#Tier 1-2
upgrade(troops,"woman_n_refugee","woman_n_camp_follower")
upgrade(troops,"woman_n_peasant","woman_n_camp_follower")
upgrade(troops,"woman_n_extra1","woman_n_camp_follower")
upgrade(troops,"woman_n_extra2","woman_n_camp_follower")
upgrade(troops,"woman_n_extra3","woman_n_camp_follower")
upgrade(troops,"woman_n_extra4","woman_n_camp_follower")
upgrade(troops,"woman_n_extra5","woman_n_camp_follower")
#Tier 2-3
upgrade(troops,"woman_n_camp_follower","woman_n_huntress")
#Tier 3-4
upgrade(troops,"woman_n_huntress","woman_n_maiden")
#Tier 4-5
upgrade(troops,"woman_n_maiden","woman_n_swob_ridder")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"woman_r_refugee","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_peasant","woman_r_camp_follower","woman_r_dressed_up")
upgrade2(troops,"woman_r_extra1","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra2","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra3","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra4","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra5","woman_r_militia","woman_r_camp_follower")
#Tier 2-3
upgrade(troops,"woman_r_militia","woman_r_warrior")
upgrade(troops,"woman_r_camp_follower","woman_r_huntress")
upgrade(troops,"woman_r_dressed_up","woman_r_stedinger")
#Tier 3-4
upgrade(troops,"woman_r_warrior","woman_r_truus_te_paard")
upgrade2(troops,"woman_r_huntress","woman_r_markswoman","woman_r_mounted_markswoman")
upgrade(troops,"woman_r_stedinger","woman_r_kriegerin")
#Tier 4-5
upgrade(troops,"woman_r_truus_te_paard","woman_r_swob_ridder")
upgrade(troops,"woman_r_markswoman","woman_r_virago")
upgrade(troops,"woman_r_mounted_markswoman","woman_r_amazon")
upgrade(troops,"woman_r_kriegerin","woman_r_schildmaid")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"woman_e_refugee","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_peasant","woman_e_camp_follower","woman_e_dressed_up")
upgrade2(troops,"woman_e_extra1","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra2","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra3","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra4","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra5","woman_e_militia","woman_e_camp_follower")
#Tier 2-3
upgrade2(troops,"woman_e_militia","woman_e_warrior","woman_e_nurse")
upgrade(troops,"woman_e_camp_follower","woman_e_huntress")
upgrade2(troops,"woman_e_dressed_up","woman_e_stedinger","woman_e_hospitaller")
#Tier 3-4
upgrade2(troops,"woman_e_warrior","woman_e_sword_sister","woman_e_truus_te_paard")
upgrade(troops,"woman_e_nurse","woman_e_maiden")
upgrade2(troops,"woman_e_huntress","woman_e_markswoman","woman_e_mounted_markswoman")
upgrade(troops,"woman_e_stedinger","woman_e_kriegerin")
upgrade2(troops,"woman_e_hospitaller","woman_e_beritten_jungfrau","woman_e_jungfrau")
#Tier 4-5
upgrade(troops,"woman_e_truus_te_paard","woman_e_swob_ridder")
upgrade(troops,"woman_e_maiden","woman_e_femme_fatale")
upgrade(troops,"woman_e_markswoman","woman_e_virago")
upgrade(troops,"woman_e_mounted_markswoman","woman_e_amazon")
upgrade(troops,"woman_e_kriegerin","woman_e_schildmaid")
upgrade(troops,"woman_e_beritten_jungfrau","woman_e_schildjungfer")
#Tier 5-6
upgrade(troops,"woman_e_swob_ridder","woman_e_kenau")
upgrade(troops,"woman_e_amazon","woman_e_black_widow")
upgrade(troops,"woman_e_schildjungfer","woman_e_walkure")
##
###

### Custom Troops
##Native troop tree
#Tier 1-2
upgrade(troops,"custom_n_recruit","custom_n_militia")
#Tier 2-3
upgrade2(troops,"custom_n_militia","custom_n_guard","custom_n_page")
#Tier 3-4
upgrade2(troops,"custom_n_guard","custom_n_swordman","custom_n_archer")
upgrade(troops,"custom_n_page","custom_n_squire")
#Tier 4-5
upgrade(troops,"custom_n_swordman","custom_n_swordmaster")
upgrade(troops,"custom_n_squire","custom_n_knight")
upgrade(troops,"custom_n_archer","custom_n_expert_archer")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"custom_r_recruit","custom_r_militia","custom_r_hunter")
#Tier 2-3
upgrade2(troops,"custom_r_militia","custom_r_guard","custom_r_page")
upgrade(troops,"custom_r_hunter","custom_r_woodsman")
#Tier 3-4
upgrade2(troops,"custom_r_guard","custom_r_swordman","custom_r_spearman")
upgrade(troops,"custom_r_page","custom_r_squire")
upgrade2(troops,"custom_r_woodsman","custom_r_archer","custom_r_skirmisher")
#Tier 4-5
upgrade(troops,"custom_r_swordman","custom_r_swordmaster")
upgrade(troops,"custom_r_squire","custom_r_knight")
upgrade(troops,"custom_r_archer","custom_r_expert_archer")
upgrade(troops,"custom_r_skirmisher","custom_r_frontline_skirmisher")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"custom_e_recruit","custom_e_militia","custom_e_hunter")
#Tier 2-3
upgrade2(troops,"custom_e_militia","custom_e_guard","custom_e_page")
upgrade2(troops,"custom_e_hunter","custom_e_page","custom_e_woodsman")
#Tier 3-4
upgrade2(troops,"custom_e_guard","custom_e_swordman","custom_e_spearman")
upgrade(troops,"custom_e_page","custom_e_squire")
upgrade2(troops,"custom_e_woodsman","custom_e_archer","custom_e_skirmisher")
#Tier 4-5
upgrade(troops,"custom_e_swordman","custom_e_swordmaster")
upgrade(troops,"custom_e_spearman","custom_e_spearmaster")
upgrade2(troops,"custom_e_squire","custom_e_knight","custom_e_horse_archer")
upgrade(troops,"custom_e_archer","custom_e_expert_archer")
upgrade(troops,"custom_e_skirmisher","custom_e_frontline_skirmisher")
#Tier 5-6
upgrade(troops,"custom_e_knight","custom_e_heavy_knight")
upgrade(troops,"custom_e_horse_archer","custom_e_heavy_horse_archer")
##

# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = { "troops" : troops }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end