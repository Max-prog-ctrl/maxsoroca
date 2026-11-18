import html, json

pass

W = 46
def dots(items):
    out = []
    for i, t in enumerate(items, 1):
        n = f"{i:03d}"
        out.append(n + " " + "." * max(3, W - 5 - len(t)) + " " + t)
    return "\n".join(out)

sections = {
    "pictures": ["HOTEL_HILBERT", "FAG_BUTTS_IN_THE_FIRE_BUCKET", "BUBBLE_BOY", "INSANE_IN_THE_BRANE",
                 "SULETHI", "KŘIŽERKI", "INSULARITY", "CHAPÜLÉE", "IVERIA [wip]",
                 "RETIRER_D'EN_BAS_DE_L'EAU [wip]", "CHOPPER 2+1 [wip]", "ANITA [wip]",
                 "THE_OBSERVER_EFFECT [wip]", "DJINNOLOGY [wip]", "AZDAJA [wip]"],
    "talks": ["FRIEDER_NAKE", "JANINA_LOH", "TORSTEN_ENSSLIN", "ZOE_HATZIYANNAKI",
              "ALBRECHT_BEUTELSPACHER", "WILLI_XYLANDER", "ROSA_MENKMAN"],
    "spaces": ["CAUCASUS", "BELARUS", "COCOONS", "CHIȘINĂU", "GORNO-BADAKHSHAN", "BEOGRAD", "GAGAUZIA",
               "TRANSNISTRIA", "SOROCA", "BAM", "HASANKEYF", "PERSIA", "KURDISTAN", "KUTAISI", "UKRAJINA",
               "OGYGIA", "ISSYK-KUL", "KYRGYZSTAN", "STANS", "YAZD", "RICHAT", "PATERNOSTER", "SELECTED_FRAMES"],
    "words": ["PLURIVERSUM", "DIE_ORDNUNG_DER_ZEIT", "KOSMISMUS", "DAS_UNIVERSUM_IN_DEINER_HAND",
              "DIE_ENTDECKUNG_DES_UNMÖGLICHEN", "UR_UND_ANDERE_ZEITEN", "UNSER_MATHEMATISCHES_UNIVERSUM",
              "DIE_KOSMISCHE_SCHLANGE", "DAS_KONNEKTOM", "GÖDEL,ESCHER,BACH", "WARUM_GOTT_DOCH_WÜRFELT",
              "WAS_IST_LEBEN?", "ES_GIBT_KEINE_MATERIE!", "IM_SPIEGEL_DER_SPRACHE",
              "DAS_GEHEIME_BEWUSSTSEIN_DER_PFLANZEN"],
    "sounds": ["IT_BEGAN_IN_EPPELSHEIM", "ES_IST_EIN_KRAUT_ENTSPRUNGEN", "DIE_LETZTE_WELT", "INSIDE/OUTSIDE",
               "WE_EXIST_IN_A_TWILIGHT_IN_BETWEEN", "STAN", "49_AUS_2020", "UPSET&RHYTHM"],
}
panels = dict(sections)
panels["IST"] = ("I . S . T\n\n"
                 "institute of serendipity & transience\n\n"
                 "status " + "." * 27 + " tba\n"
                 "location " + "." * 21 + " 51.15°N 14.99°E\n\n"
                 "° signal pending")

tpl = open('template.html').read()
spaces = json.load(open('spaces.json'))
out = tpl.replace("%%PANELS%%", json.dumps(panels, ensure_ascii=False)).replace("%%SPACES%%", json.dumps(spaces, ensure_ascii=False)).replace("%%WORKS%%", json.dumps(json.load(open("works.json")), ensure_ascii=False))
open('index.html', 'w').write(out)
print(len(out))
