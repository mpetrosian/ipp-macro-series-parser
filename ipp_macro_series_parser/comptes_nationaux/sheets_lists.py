# -*- coding: utf-8 -*-


# TaxIPP -- A french microsimulation model
# By: IPP <taxipp@oipp.eu>
#
# Copyright (C) 2012, 2013, 2014, 2015 IPP
# https://github.com/taxipp
#
# This file is part of TaxIPP.
#
# TaxIPP is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# TaxIPP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
log = logging.getLogger(__name__)


# CN1

input_CN1 = {
    # Revenus versés par reste du monde
    'Salaires_verses_au_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Salaires_verses_par_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Interets_verses_par_rdm': {'code': 'D41', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Dividendes_verses_par_rdm_D42': {'code': 'D42', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Dividendes_verses_par_rdm_D43': {'code': 'D43', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Interets_verses_au_rdm': {'code': 'D41', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Dividendes_verses_au_rdm_D42': {'code': 'D42', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Dividendes_verses_au_rdm_D43': {'code': 'D43', 'institution': 'S2', 'ressources': True, 'drop': True},
    # Dépréciation du capital fixe (CCF) : économie nationale, APUs, ISBLSM
    # 'Consommation_de_capital_fixe _-_APU': {'code': 'P51c', 'institution': 'S13', 'ressources': False},
    # 'Consommation_de_capital_fixe _-_ISBLSM': {'code': 'P51c', 'institution': 'S15', 'ressources': False},
    # Variables CN2, nécessaires pour reconstruction du Revenu national façon Piketty
    'Sal_verses_SNF': {'code': 'D11', 'institution': 'S11', 'ressources': False, 'drop': True},
    'Sal_verses_SF': {'code': 'D11', 'institution': 'S12', 'ressources': False, 'drop': True},
    'Sal_verses_par_APU': {'code': 'D11', 'institution': 'S13', 'ressources': False, 'drop': True},
    'Sal_verses_par_menages': {'code': 'D11', 'institution': 'S14', 'ressources': False, 'drop': True},
    'Sal_verses_par_ISBLSM': {'code': 'D11', 'institution': 'S15', 'ressources': False, 'drop': True},
    'ene_menages': {'code': 'B2n', 'institution': 'S14', 'ressources': False, 'drop': True},
    'Revenu_mixte_net_des_menages_non_salaries': {'code': 'B3n', 'institution': 'S1', 'ressources': False,
                                                  'drop': True},
    'cs_eff_empl_SNF': {'code': 'D121', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_eff_empl_SF': {'code': 'D121', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_eff_empl_APU': {'code': 'D121', 'institution': 'S13', 'ressources': False, 'drop': True},
    'cs_eff_empl_Menages': {'code': 'D121', 'institution': 'S14', 'ressources': False, 'drop': True},
    'cs_eff_empl_ISBLSM': {'code': 'D121', 'institution': 'S15', 'ressources': False, 'drop': True},
    'cs_imput_empl_SNF': {'code': 'D122', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_imput_empl_SF': {'code': 'D122', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_imput_empl_APU': {'code': 'D122', 'institution': 'S13', 'ressources': False, 'drop': True},
    'cs_imput_empl_Menages': {'code': 'D122', 'institution': 'S14', 'ressources': False, 'drop': True},
    # 'cs_imput_empl_ISBLSM': {'code': 'D122', 'institution': 'S15', 'ressources': False, 'drop': True},  # n'existe pas
    # Excedent_net_d_exploitation_ENE_SNF
    'ene_snf': {'code': 'B2n', 'institution': 'S11', 'ressources': False, 'description': '', 'drop': True},
    'ene_sf': {'code': 'B2n', 'institution': 'S12', 'ressources': False, 'description': '', 'drop': True},
    'Impots_sur_les_produits_ressources_APU': {'code': 'D21', 'institution': 'S13', 'ressources': True,
                                               'drop': True},
    'Subventions_sur_les_produits_ressources_APU': {'code': 'D31', 'institution': 'S13', 'ressources': True,
                                                    'drop': True},
    'Autres_impots_sur_la_production_ressources_APU': {'code': 'D29', 'institution': 'S13', 'ressources': True,
                                                       'drop': True},
    'Autres_subventions_sur_la_production_ressources_APU': {'code': 'D39', 'institution': 'S13', 'ressources': True,
                                                            'drop': True}
    }

input_CN1_base_2010 = {
    'Consommation_de_capital_fixe_economie_nationale': {'code': 'P51c', 'institution': 'S1', 'ressources': False},
    'Produit_interieur_brut_PIB': {'code': None, 'institution': 'S1', 'ressources': False, 'description': 'PIB'},
    'Produit_interieur_net_PIN': {'code': None, 'institution': 'S1', 'ressources': False, 'description': 'PIN'},
    'Revenu_national_brut': {'code': None, 'institution': 'S1', 'ressources': False,
                             'description': 'revenu national brut en milliards d'},
    'Revenus_de_la_propriete_verses_par_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Revenus_de_la_propriete_verses_au_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': True, 'drop': True},
    }

input_CN1_base_2005 = {
    'Consommation_de_capital_fixe_economie_nationale': {'code': 'K1', 'institution': 'S1', 'ressources': False},
    'Produit_interieur_brut_PIB': {'code': None, 'institution': 'S1', 'ressources': False, 'description': 'PIB'},
    'Produit_interieur_net_PIN': {'code': None, 'institution': 'S1', 'ressources': False, 'description': 'PIN'},
    'Revenu_national_brut': {'code': None, 'institution': 'S1', 'ressources': False,
                             'description': 'revenu national brut en milliards d'},
    'Autres_revenus_investissements_verses_au_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': True,
                                                     'drop': True},
    }

input_CN1_base_2000 = {
    'Consommation_de_capital_fixe_economie_nationale': {'code': 'K1', 'institution': 'S1', 'ressources': False},
    'Produit_interieur_brut_PIB': {'code': None, 'institution': 'S1', 'ressources': False,
                                   'description': 'Valeur ajoutée brute'},
    'Produit_interieur_net_PIN': {'code': None, 'institution': 'S1', 'ressources': False,
                                  'description': 'Valeur ajoutée nette'},
    'Revenu_national_brut': {'code': None, 'institution': 'S1', 'ressources': False,
                             'description': 'Total des secteurs résidents'},
    'Revenus_propriete_aux_assures_verses_au_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': True,
                                                     'drop': True},
    }

formulas_CN1_base_2010 = {
    'Interets_et_dividendes_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Interets_verses_par_rdm + Dividendes_verses_par_rdm_D42 + Dividendes_verses_par_rdm_D43 + Revenus_de_la_propriete_verses_par_rdm - Interets_verses_au_rdm - Dividendes_verses_au_rdm_D42 - Dividendes_verses_au_rdm_D43 - Revenus_de_la_propriete_verses_au_rdm',
        'drop': True
        },
    }
formulas_CN1_base_2005 = {
    'Interets_et_dividendes_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Interets_verses_par_rdm + Dividendes_verses_par_rdm_D42 + Dividendes_verses_par_rdm_D43 - Interets_verses_au_rdm - Dividendes_verses_au_rdm_D42 - Dividendes_verses_au_rdm_D43 - Autres_revenus_investissements_verses_au_rdm',
        'drop': True
        },
    }
formulas_CN1_base_2000 = {
    'Interets_et_dividendes_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Interets_verses_par_rdm + Dividendes_verses_par_rdm_D42 + Dividendes_verses_par_rdm_D43 - Interets_verses_au_rdm - Dividendes_verses_au_rdm_D42 - Dividendes_verses_au_rdm_D43 - Revenus_propriete_aux_assures_verses_au_rdm',
        'drop': True
        },
    }
formulas_CN1 = {
    'Profits_des_societes': {
        'formula': 'ene_snf + ene_sf',
        'drop': True
        },
    'Sal_cs_verses_societes': {
        'formula': 'Sal_verses_SNF + Sal_verses_SF + cs_eff_empl_SNF + cs_eff_empl_SF + cs_imput_empl_SNF + cs_imput_empl_SF',
        'drop': True
        },
    'VA_Societes': {
        'formula': 'Profits_des_societes + Sal_cs_verses_societes',
        'drop': True
        },
    'VA_Immobilier_Loyers': {
        'formula': 'ene_menages',
        'drop': True
        },
    'Revenu_d_activite_des_non_salaries': {
        'formula': 'Revenu_mixte_net_des_menages_non_salaries',
        'drop': True
        },
    'Salaires_et_cot_soc_verses_par_les_non_salaries_et_les_menages': {
        'formula': 'Sal_verses_par_menages + cs_eff_empl_Menages + cs_imput_empl_Menages',
        'drop': True
        },
    'VA_APU_et_ISBLSM': {
        'formula': 'Sal_verses_par_APU + Sal_verses_par_ISBLSM + cs_eff_empl_APU + cs_eff_empl_ISBLSM + cs_imput_empl_APU',  #  + cs_imput_empl_ISBLSM
        'drop': True
        },
    'Impots_indirects': {
        'formula': 'Impots_sur_les_produits_ressources_APU - Subventions_sur_les_produits_ressources_APU + Autres_impots_sur_la_production_ressources_APU - Autres_subventions_sur_la_production_ressources_APU',
        'drop': True
        },
    '%_Produit_interieur_net_/_Revenu_national': {
        'formula': 'Produit_interieur_net_PIN / Revenu_national_brut'
        },
    '%_Revenus_reste_du_monde_/_Revenu_national': {
        'formula': 'Revenus_verses_par_rdm_nets / Revenu_national_brut'
        },
    # 'Depreciation_du_capital_(CCF)': {
    #     'formula': 'Consommation_de_capital_fixe _-_APU + Consommation_de_capital_fixe _-_ISBLSM + '},
    'CCF_/_PIB': {
        'formula': 'Consommation_de_capital_fixe_economie_nationale / Produit_interieur_brut_PIB'
        },  # voir si on utilise la CCF Piketty (à calculer)
    # 'Taux_de_croissance_du_PIB_entre_l_annee_N-2_et_l_annee_N-1'
    '%_Revenu_national_/_PIB': {
        'formula': 'Revenu_national_brut / Produit_interieur_brut_PIB'
        },  # voir si on prend plutôt le RNB Piketty
    'Salaires_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Salaires_verses_par_rdm - Salaires_verses_au_rdm',
        'drop': True
        },
    'Revenus_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Salaires_verses_par_rdm_nets + Interets_et_dividendes_verses_par_rdm_nets',
        },
    'Revenu_national_Piketty': {
        'formula': 'VA_Societes + VA_Immobilier_Loyers + Revenu_d_activite_des_non_salaries + Salaires_et_cot_soc_verses_par_les_non_salaries_et_les_menages + VA_APU_et_ISBLSM + Impots_indirects + Revenus_verses_par_rdm_nets'
        },
    }


def generate_CN1_variables(year):
    variables_CN1 = input_CN1.copy()
    variables_CN1.update(formulas_CN1)
    if year in range(2004, 2010):
        variables_CN1.update(input_CN1_base_2000)
        variables_CN1.update(formulas_CN1_base_2000)
        log.info('Sheet-creation not optimized for data of base 2000 and under : missing non-tee files > missing data')
    if year in range(2010, 2013):
        variables_CN1.update(input_CN1_base_2005)
        variables_CN1.update(formulas_CN1_base_2005)
    if year > 2012:
        variables_CN1.update(input_CN1_base_2010)
        variables_CN1.update(formulas_CN1_base_2010)
    return variables_CN1


# CN2

input_CN2 = {
    # Revenus versés par reste du monde
    'Salaires_verses_au_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Salaires_verses_par_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Interets_verses_par_rdm': {'code': 'D41', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Dividendes_verses_par_rdm_D42': {'code': 'D42', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Dividendes_verses_par_rdm_D43': {'code': 'D43', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Interets_verses_au_rdm': {'code': 'D41', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Dividendes_verses_au_rdm_D42': {'code': 'D42', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Dividendes_verses_au_rdm_D43': {'code': 'D43', 'institution': 'S2', 'ressources': True, 'drop': True},
    'Sal_verses_SNF': {'code': 'D11', 'institution': 'S11', 'ressources': False, 'drop': True},
    'Sal_verses_SF': {'code': 'D11', 'institution': 'S12', 'ressources': False, 'drop': True},
    'Sal_verses_par_APU': {'code': 'D11', 'institution': 'S13', 'ressources': False, 'drop': True},
    'Sal_verses_par_menages': {'code': 'D11', 'institution': 'S14', 'ressources': False, 'drop': True},
    'Sal_verses_par_ISBLSM': {'code': 'D11', 'institution': 'S15', 'ressources': False, 'drop': True},
    'ene_menages': {'code': 'B2n', 'institution': 'S14', 'ressources': False, 'drop': True},
    'Revenu_mixte_net_des_menages_non_salaries': {'code': 'B3n', 'institution': 'S1', 'ressources': False,
                                                  'drop': True},
    'cs_eff_empl_SNF': {'code': 'D121', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_eff_empl_SF': {'code': 'D121', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_eff_empl_APU': {'code': 'D121', 'institution': 'S13', 'ressources': False, 'drop': True},
    'cs_eff_empl_Menages': {'code': 'D121', 'institution': 'S14', 'ressources': False, 'drop': True},
    'cs_eff_empl_ISBLSM': {'code': 'D121', 'institution': 'S15', 'ressources': False, 'drop': True},
    'cs_imput_empl_SNF': {'code': 'D122', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_imput_empl_SF': {'code': 'D122', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_imput_empl_APU': {'code': 'D122', 'institution': 'S13', 'ressources': False, 'drop': True},
    'cs_imput_empl_Menages': {'code': 'D122', 'institution': 'S14', 'ressources': False, 'drop': True},
    # 'cs_imput_empl_ISBLSM': {'code': 'D122', 'institution': 'S15', 'ressources': False, 'drop': True},  # n'existe pas
    'ene_snf': {'code': 'B2n', 'institution': 'S11', 'ressources': False, 'description': '', 'drop': True},
    'ene_sf': {'code': 'B2n', 'institution': 'S12', 'ressources': False, 'description': '', 'drop': True},
    'Impots_sur_les_produits_ressources_APU': {'code': 'D21', 'institution': 'S13', 'ressources': True,
                                               'drop': True},
    'Subventions_sur_les_produits_ressources_APU': {'code': 'D31', 'institution': 'S13', 'ressources': True,
                                                    'drop': True},
    'Autres_impots_sur_la_production_ressources_APU': {'code': 'D29', 'institution': 'S13', 'ressources': True,
                                                       'drop': True},
    'Autres_subventions_sur_la_production_ressources_APU': {'code': 'D39', 'institution': 'S13', 'ressources': True,
                                                            'drop': True}
    }

input_CN2_base_2010 = {
    'Revenus_de_la_propriete_verses_par_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': False, 'drop': True},
    'Revenus_de_la_propriete_verses_au_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': True, 'drop': True},
    }
input_CN2_base_2005 = {
    'Autres_revenus_investissements_verses_au_rdm': {'code': 'D44', 'institution': 'S2', 'ressources': True,
                                                     'drop': True},
    }

formulas_CN2_base_2010 = {
    'Interets_et_dividendes_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Interets_verses_par_rdm + Dividendes_verses_par_rdm_D42 + Dividendes_verses_par_rdm_D43 + Revenus_de_la_propriete_verses_par_rdm - Interets_verses_au_rdm - Dividendes_verses_au_rdm_D42 - Dividendes_verses_au_rdm_D43 - Revenus_de_la_propriete_verses_au_rdm',
        },
    }
formulas_CN2_base_2005 = {
    'Interets_et_dividendes_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Interets_verses_par_rdm + Dividendes_verses_par_rdm_D42 + Dividendes_verses_par_rdm_D43 - Interets_verses_au_rdm - Dividendes_verses_au_rdm_D42 - Dividendes_verses_au_rdm_D43 - Autres_revenus_investissements_verses_au_rdm',
        },
    }
formulas_CN2 = {
    'Profits_des_societes': {
        'formula': 'ene_snf + ene_sf',
        },
    'Sal_cs_verses_societes': {
        'formula': 'Sal_verses_SNF + Sal_verses_SF + cs_eff_empl_SNF + cs_eff_empl_SF + cs_imput_empl_SNF + cs_imput_empl_SF',
        },
    'VA_Societes': {
        'formula': 'Profits_des_societes + Sal_cs_verses_societes',
        },
    'VA_Immobilier_Loyers': {
        'formula': 'ene_menages',
        },
    'Revenu_d_activite_des_non_salaries': {
        'formula': 'Revenu_mixte_net_des_menages_non_salaries',
        },
    'Salaires_et_cot_soc_verses_par_les_non_salaries_et_les_menages': {
        'formula': 'Sal_verses_par_menages + cs_eff_empl_Menages + cs_imput_empl_Menages',
        },
    'VA_APU_et_ISBLSM': {
        'formula': 'Sal_verses_par_APU + Sal_verses_par_ISBLSM + cs_eff_empl_APU + cs_eff_empl_ISBLSM + cs_imput_empl_APU',  #  + cs_imput_empl_ISBLSM
        },
    'Impots_indirects': {
        'formula': 'Impots_sur_les_produits_ressources_APU - Subventions_sur_les_produits_ressources_APU + Autres_impots_sur_la_production_ressources_APU - Autres_subventions_sur_la_production_ressources_APU',
        },
    'Salaires_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Salaires_verses_par_rdm - Salaires_verses_au_rdm',
        },
    'Revenus_verses_par_rdm_nets': {
        'code': None,
        'institution': 'S2',
        'ressources': False,
        'formula': 'Salaires_verses_par_rdm_nets + Interets_et_dividendes_verses_par_rdm_nets',
        'drop': True
        },
    'Revenu_national_Piketty': {
        'formula': 'VA_Societes + VA_Immobilier_Loyers + Revenu_d_activite_des_non_salaries + Salaires_et_cot_soc_verses_par_les_non_salaries_et_les_menages + VA_APU_et_ISBLSM + Impots_indirects + Revenus_verses_par_rdm_nets'},
    }


def generate_CN2_variables(year):
    variables_CN2 = input_CN2.copy()
    variables_CN2.update(formulas_CN2)
    if year in range(2010, 2013) :
        variables_CN2.update(input_CN2_base_2005)
        variables_CN2.update(formulas_CN2_base_2005)
    if year > 2012 :
        variables_CN2.update(input_CN2_base_2010)
        variables_CN2.update(formulas_CN2_base_2010)
    else:
        log.info('Sheet-creation not optimized for data of base 2000 and under : missing non-tee files > missing data')
    return variables_CN2


# CN11

input_CN11 = {
    'Sal_verses_SNF': {'code': 'D11', 'institution': 'S11', 'ressources': False},
    'Sal_verses_SF': {'code': 'D11', 'institution': 'S12', 'ressources': False},
    'cs_eff_empl_SNF': {'code': 'D121', 'institution': 'S11', 'ressources': False},
    'cs_eff_empl_SF': {'code': 'D121', 'institution': 'S12', 'ressources': False},
    'cs_imput_empl_SNF': {'code': 'D122', 'institution': 'S11', 'ressources': False},
    'cs_imput_empl_SF': {'code': 'D122', 'institution': 'S12', 'ressources': False},
    'Sal_verses_par_menages': {'code': 'D11', 'institution': 'S14', 'ressources': False},
    'cs_eff_empl_Menages': {'code': 'D121', 'institution': 'S14', 'ressources': False},
    'cs_imput_empl_Menages': {'code': 'D122', 'institution': 'S14', 'ressources': False},
    'Sal_verses_par_APU': {'code': 'D11', 'institution': 'S13', 'ressources': False},
    'Sal_verses_par_ISBLSM': {'code': 'D11', 'institution': 'S15', 'ressources': False},
    'cs_eff_empl_APU': {'code': 'D121', 'institution': 'S13', 'ressources': False},
    'cs_eff_empl_ISBLSM': {'code': 'D121', 'institution': 'S15', 'ressources': False},
    'cs_imput_empl_APU': {'code': 'D122', 'institution': 'S13', 'ressources': False},
    'cs_imput_empl_ISBLSM': {'code': 'D122', 'institution': 'S15', 'ressources': False},
    'Salaires_verses_par_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': False},
    'Salaires_verses_au_rdm': {'code': 'D11', 'institution': 'S2', 'ressources': True},
    'cs_eff_empl_versees_par_rdm': {'code': 'D121', 'institution': 'S2', 'ressources': False},
    'cs_eff_empl_versees_au_rdm': {'code': 'D121', 'institution': 'S2', 'ressources': True},
    # 'cs_imput_empl_versees_par_rdm': {'code': 'D122', 'institution': 'S2', 'ressources': False},  # n'existe pas
    # 'cs_imput_empl_versees_au_rdm': {'code': 'D122', 'institution': 'S2', 'ressources': True},  # n'existe pas
    'cs_imput_empl_recues_par_admin_oblig': {'code': 'D612', 'institution': 'S13', 'ressources': True},
    }

input_CN11_base_2005 = input_CN11.copy()
input_CN11_base_2005.update(
    {'cs_eff_empl_recues_par_admin_oblig': {'code': 'D6111', 'institution': 'S13', 'ressources': True}})

input_CN11_base_2010 = input_CN11.copy()
input_CN11_base_2010.update(
    {'cs_eff_empl_recues_par_admin_oblig': {'code': 'D611', 'institution': 'S13', 'ressources': True}})

formulas_CN11 = {
    # PRIVE
    'Sal_bruts_secteur_prive': {
        'formula': 'Sal_verses_SNF + Sal_verses_SF + Sal_verses_par_menages + Salaires_verses_par_rdm - Salaires_verses_au_rdm'
        },

    # cs patronales obligatoires
    #    pour colonne C
    'cs_patronales_effectives_public': {
        'formula': 'cs_eff_empl_APU + cs_eff_empl_ISBLSM'
        },
    'cs_patronales_effectives_prive_oblig' : {
        'formula': 'cs_eff_empl_recues_par_admin_oblig - cs_patronales_effectives_public'
        },
    #   pour colonne D
    'cs_patronales_imputees_public': {
        'formula': 'cs_imput_empl_APU + cs_imput_empl_ISBLSM'
        },
    'cs_patronales_imputees_prive_oblig': {  # doit être égal à 0 car uniquement dans le public où il y a des imputées obligatoires
        'formula': 'cs_imput_empl_recues_par_admin_oblig - cs_patronales_imputees_public'
        },
    #   colonne E
    'taux_cs_patronales_prive_oblig': {
        'formula': '( cs_patronales_effectives_prive_oblig + cs_patronales_imputees_prive_oblig) / Sal_bruts_secteur_prive'
        },

    # cs patronales facultatives
    #   colonne F
    'total_cs_empl_eff_versees': {
        'formula': 'cs_eff_empl_SNF + cs_eff_empl_SF + cs_eff_empl_APU + cs_eff_empl_ISBLSM + cs_eff_empl_Menages + cs_eff_empl_versees_par_rdm - cs_eff_empl_versees_au_rdm'
        },
    'cs_patronales_eff_facultatives': {  # ex cs_patr_eff_prive_facultatives
        'formula': 'total_cs_empl_eff_versees - cs_eff_empl_recues_par_admin_oblig'
        },  # en réalité viennent toutes du privé, car pas de facultatives dans le public je crois
    #   colonne G
    'total_cs_empl_imput_versees': {
        'formula': 'cs_imput_empl_SNF + cs_imput_empl_SF + cs_imput_empl_APU + cs_imput_empl_ISBLSM + cs_imput_empl_Menages'  #  + cs_imput_empl_versees_par_rdm - cs_imput_empl_versees_au_rdm (n'existent pas)
        },
    'cs_patronales_imput_facultatives': {  # ex cs_patronales_imput_prive_facultatives
        'formula': 'total_cs_empl_imput_versees - cs_imput_empl_recues_par_admin_oblig'
        },
    #   colonne H
    'taux_cs_patronales_facult_prive': {
        'formula': '( cs_patronales_eff_facultatives + cs_patronales_imput_facultatives ) / Sal_bruts_secteur_prive'
        },

    # PUBLIC
    'Sal_bruts_secteur_public': {
        'formula': 'Sal_verses_par_APU + Sal_verses_par_ISBLSM'
        },
    'taux_cs_patronales_public': {
        'formula': '( cs_patronales_effectives_public + cs_patronales_imput_facultatives ) / Sal_bruts_secteur_public'
        },

    # TOTAUX
    'total_salaires': {
        'formula': 'Sal_bruts_secteur_prive + Sal_bruts_secteur_public'
        },
    'total_cs_patronales_eff_oblig': {  # doit être égal à cs_eff_empl_recues_par_admin_oblig
        'formula': 'cs_patronales_effectives_prive_oblig + cs_patronales_effectives_public'
        },
    'total_cs_patronales_imput_oblig': {  # doit être égal à cs_imput_empl_recues_par_admin_oblig
        'formula' : 'cs_patronales_imputees_prive_oblig + cs_patronales_imputees_public'
        },
    'taux_cs_patronales_oblig': {
        'formula': '( total_cs_patronales_eff_oblig + total_cs_patronales_imput_oblig ) / total_salaires'
        },
    'total_cs_patronales_eff_facult': {
        'formula': 'cs_patronales_eff_facultatives'
        },
    'total_cs_patronales_imput_facult': {
        'formula': 'cs_patronales_imput_facultatives'
        },
    'taux_cs_patronales_facult': {
        'formula': '( total_cs_patronales_eff_facult + cs_patronales_imput_facultatives ) / total_salaires'
        },

    # AUTRES
    # SNF
    'taux_cs_patronales_SNF': {
        'formula': '( cs_eff_empl_SNF + cs_imput_empl_SNF ) / Sal_verses_SNF'
        },
    # SF
    'taux_cs_patronales_SF': {
        'formula': '( cs_eff_empl_SF + cs_imput_empl_SF ) / Sal_verses_SF'
        },
    # APU
    'taux_cs_patronales_APU': {
        'formula': '( cs_eff_empl_APU + cs_imput_empl_APU ) / Sal_verses_par_APU'
        },
    # ISBLSM
    'taux_cs_patronales_ISBLSM': {
        'formula': '( cs_eff_empl_ISBLSM + cs_imput_empl_ISBLSM ) / Sal_verses_par_ISBLSM'
        },
    # Ménages
    'taux_cs_patronales_Menages': {
        'formula': '( cs_eff_empl_Menages + cs_imput_empl_Menages)/ Sal_verses_par_menages'
        },
    # versé par rdm
    'taux_cs_patronales_par_rdm': {
        'formula': '( cs_eff_empl_versees_par_rdm ) / Salaires_verses_par_rdm'  # + cs_imput_empl_versees_par_rdm (n'existent pas)
        },
    # versé au rdm
    'taux_cs_patronales_au_rdm': {
        'formula': '( cs_eff_empl_versees_au_rdm) / Salaires_verses_au_rdm'  #  + cs_imput_empl_versees_au_rdm (n'existe pas)
        },
    # -Privé-
    'cs_patronales_eff_prive': {
        'formula': 'cs_eff_empl_SNF + cs_eff_empl_SF + cs_eff_empl_Menages + cs_eff_empl_versees_par_rdm - cs_eff_empl_versees_au_rdm'
        },
    'cs_patronales_imput_prive': {  # doit être égal à cs_patronales_imput_facultatives (puisque toutes les imput privées sont facultatives) ou encore à total_cs_patronales_imput_facult (car toutes les imput facult sont dans le privé)
        'formula': 'cs_imput_empl_SNF + cs_imput_empl_SF + cs_imput_empl_Menages'  #  + cs_imput_empl_versees_par_rdm - cs_imput_empl_versees_au_rdm (n'existent pas)
        },
    'taux_cs_patronales_prive': {
        'formula': '( cs_patronales_eff_prive + cs_patronales_imput_prive) / Sal_bruts_secteur_prive'
        },
    # -oblig. + facult.-
    'total_cs_patronales_eff': {  # (obl. + facult.)
        'formula': 'total_cs_patronales_eff_oblig + total_cs_patronales_eff_facult'
        },
    'total_cs_patronales_imput': {  # (obl. + facult.)
        'formula': 'total_cs_patronales_imput_oblig + total_cs_patronales_imput_facult'
        },

    }


def generate_CN11_variables(year):
    if year in range(2010, 2013):
        variables_CN11 = input_CN11_base_2005.copy()
    if year > 2012:
        variables_CN11 = input_CN11_base_2010.copy()
    variables_CN11.update(formulas_CN11)
    return variables_CN11


# CN12

input_CN12 = {
    'cs_eff_empl_SNF': {'code': 'D121', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_eff_empl_SF': {'code': 'D121', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_eff_empl_Menages': {'code': 'D121', 'institution': 'S14', 'ressources': False, 'drop': True},
    'cs_eff_empl_APU': {'code': 'D121', 'institution': 'S13', 'ressources': False, 'drop': True},
    'cs_eff_empl_ISBLSM': {'code': 'D121', 'institution': 'S15', 'ressources': False, 'drop': True},
    'cs_eff_empl_versees_par_rdm': {'code': 'D121', 'institution': 'S2', 'ressources': False, 'drop': True},
    'cs_eff_empl_versees_au_rdm': {'code': 'D121', 'institution': 'S2', 'ressources': True, 'drop': True},
    'cs_imput_empl_SNF': {'code': 'D122', 'institution': 'S11', 'ressources': False, 'drop': True},
    'cs_imput_empl_SF': {'code': 'D122', 'institution': 'S12', 'ressources': False, 'drop': True},
    'cs_imput_empl_Menages': {'code': 'D122', 'institution': 'S14', 'ressources': False, 'drop': True},
    'cs_imput_empl_APU': {'code': 'D122', 'institution': 'S13', 'ressources': False, 'drop': True},
    # 'cs_imput_empl_ISBLSM': {'code': 'D122', 'institution': 'S15', 'ressources': False, 'drop': True},  # n'existe pas
    'Salaires_bruts': {'code': 'D11', 'institution': 'S1', 'ressources': True},
    'revenu_mixte_net_non_salaries': {'code': 'B3n', 'institution': 'S1', 'ressources': False},
    'cs_imput_empl_recues_par_admin_oblig': {'code': 'D612', 'institution': 'S13', 'ressources': True, 'drop': True},
    }


input_CN12_base_2005 = {
    'revenu_mixte_brut_non_salaries': {'code': 'B3', 'institution': 'S1', 'ressources': False},
    'cs_salariales_versees_par_menages': {'code': 'D6112', 'institution': 'S14', 'ressources': False},
    'cs_salariales_recues_par_admin_oblig': {'code': 'D6112', 'institution': 'S13', 'ressources': True},
    'cs_non_salaries_versees_par_menages': {'code': 'D6113', 'institution': 'S14', 'ressources': False},
    'cs_non_salaries_recues_par_admin_oblig': {'code': 'D6113', 'institution': 'S13', 'ressources': True},
    'autres_revenus_distribues_des_societes': {'code': 'D4222', 'institution': 'S14', 'ressources': True},
    'cs_eff_empl_recues_par_admin_oblig': {'code': 'D6111', 'institution': 'S13', 'ressources': True, 'drop': True},
    }

input_CN12_base_2010 = {
    'revenu_mixte_brut_non_salaries': {'code': 'B3g', 'institution': 'S1', 'ressources': False},
    'cs_menages_versees_par_menages': {'code': 'D613', 'institution': 'S14', 'ressources': False},
    'cs_menages_recues_par_admin': {'code': 'D613', 'institution': 'S13', 'ressources': True},
    'autres_revenus_distribues_des_societes': {'code': 'D422', 'institution': 'S14', 'ressources': True},
    'cs_eff_empl_recues_par_admin_oblig': {'code': 'D611', 'institution': 'S13', 'ressources': True, 'drop': True}
    }


formulas_CN12 = {
    'B3n_+_D422': {'formula': 'revenu_mixte_net_non_salaries + autres_revenus_distribues_des_societes'},
    'CCF_non_salaries_calculee': {'formula': 'revenu_mixte_brut_non_salaries - revenu_mixte_net_non_salaries'},
    'cs_patronales_eff_facultatives': {  # en fait correspond aux 'privé' (pas de facultatives dans le public je crois)
        'formula': 'cs_eff_empl_SNF + cs_eff_empl_SF + cs_eff_empl_APU + cs_eff_empl_ISBLSM + cs_eff_empl_Menages + cs_eff_empl_versees_par_rdm - cs_eff_empl_versees_au_rdm - cs_eff_empl_recues_par_admin_oblig',
        'drop': True
        },
    'cs_patronales_imput_facultatives': {
        'formula': 'cs_imput_empl_SNF + cs_imput_empl_SF + cs_imput_empl_APU  + cs_imput_empl_Menages - cs_imput_empl_recues_par_admin_oblig',  #  + cs_imput_empl_ISBLSM
        'drop': True
        },
    'Salaires_super_bruts': {
        'formula': 'Salaires_bruts + cs_eff_empl_recues_par_admin_oblig + cs_imput_empl_recues_par_admin_oblig + cs_patronales_eff_facultatives + cs_patronales_imput_facultatives',
        'drop': True
        }
    }

formulas_CN12_base_2005 = {
    'cs_salariales_facultatives': {
        'formula': 'cs_salariales_versees_par_menages - cs_salariales_recues_par_admin_oblig'
        },
    'cs_non_salaries_facultatives': {
        'formula': 'cs_non_salaries_versees_par_menages - cs_non_salaries_recues_par_admin_oblig'
        },

    # salariés
    'taux_cs_salariales_oblig': {'formula': 'cs_salariales_recues_par_admin_oblig / Salaires_bruts'},
    'taux_cs_salariales_facult': {'formula': 'cs_salariales_facultatives / Salaires_bruts'},
    'total_cs_salariales_patronales_oblig': {
        'formula': 'cs_salariales_recues_par_admin_oblig + cs_eff_empl_recues_par_admin_oblig + cs_imput_empl_recues_par_admin_oblig'
        },
    'taux_global_cs_oblig_%superbrut': {'formula': 'total_cs_salariales_patronales_oblig / Salaires_super_bruts'},

    # non-salariés
    'taux_cs_non_salaries_oblig': {'formula': 'cs_non_salaries_recues_par_admin_oblig / revenu_mixte_net_non_salaries'},
    'taux_cs_non_salaries_facult': {'formula': 'cs_non_salaries_facultatives / revenu_mixte_net_non_salaries'}
    }

formulas_CN12_base_2010 = {
    # totaux salariés + non-salariés nécessairement, puisque plus de distinction par la CN
    'cs_menages_facultatives': {'formula': 'cs_menages_versees_par_menages - cs_menages_recues_par_admin'},
    'revenus_menages': {'formula': 'Salaires_bruts + revenu_mixte_net_non_salaries'},
    'cs_menages_oblig': {'formula': 'cs_menages_recues_par_admin'},
    'taux_cs_menages_oblig': {'formula': 'cs_menages_oblig / revenus_menages'},
    'taux_cs_menages_facult': {'formula': 'cs_menages_facultatives / revenus_menages'}
    }


def generate_CN12_variables(year):
    if year in range(2010, 2013):
        variables_CN12 = input_CN12.copy()
        variables_CN12.update(input_CN12_base_2005)
        variables_CN12.update(formulas_CN12)
        variables_CN12.update(formulas_CN12_base_2005)
    if year > 2012:
        variables_CN12 = input_CN12.copy()
        variables_CN12.update(input_CN12_base_2010)
        variables_CN12.update(formulas_CN12)
    return variables_CN12
