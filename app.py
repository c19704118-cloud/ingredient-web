from flask import Flask, render_template, request

app = Flask(__name__)

# 完整扩充成分库：英文键、中文名称、风险、说明、禁忌肤质
ingredient_risk = {
    "alcohol": {
        "cn_name": "乙醇/酒精",
        "risk": "high",
        "desc": "高刺激，快速挥发带走皮肤水分，破坏皮肤屏障，加重泛红脱皮",
        "bad_for": ["敏感肌", "油敏肌", "脂溢性皮炎", "屏障受损肌"]
    },
    "fragrance": {
        "cn_name": "香精",
        "risk": "high",
        "desc": "顶级致敏成分，极易诱发痘痘、红痒、皮炎",
        "bad_for": ["痘肌", "油敏肌", "泛红敏感肌", "脂溢性皮炎"]
    },
    "ethanol": {
        "cn_name": "乙醇",
        "risk": "high",
        "desc": "和酒精为同一种物质，刺激性强，长期使用皮肤变薄",
        "bad_for": ["敏感肌", "油敏肌", "脂溢性皮炎"]
    },
    "salicylic acid": {
        "cn_name": "水杨酸",
        "risk": "medium",
        "desc": "疏通毛孔控油，高浓度会剥脱角质，屏障弱会刺痛脱皮",
        "bad_for": ["干敏肌", "破损泛红肌肤", "换季敏感期"]
    },
    "niacinamide": {
        "cn_name": "烟酰胺",
        "risk": "medium",
        "desc": "控油提亮，5%以上浓度易产生不耐受、灼热泛红",
        "bad_for": ["重度敏感肌", "屏障破损肌肤", "玫瑰痤疮"]
    },
    "benzyl alcohol": {
        "cn_name": "苯甲醇",
        "risk": "medium",
        "desc": "防腐溶剂，具有刺激性，容易刺痛眼周、泛红",
        "bad_for": ["敏感肌", "油敏皮炎肌"]
    },
    "glycerin": {
        "cn_name": "甘油",
        "risk": "low",
        "desc": "温和保湿，全肤质适配，几乎无刺激",
        "bad_for": []
    },
    "hyaluronic acid": {
        "cn_name": "透明质酸/玻尿酸",
        "risk": "low",
        "desc": "深层补水修护，温和安全",
        "bad_for": []
    },
    "phenoxyethanol": {
        "cn_name": "苯氧乙醇",
        "risk": "medium",
        "desc": "常用防腐剂，高浓度会产生灼热刺痛感",
        "bad_for": ["薄皮敏感肌", "眼周脆弱肌肤"]
    },
    "isopropyl myristate": {
        "cn_name": "肉豆蔻酸异丙酯",
        "risk": "high",
        "desc": "封闭性强，极易闷闭口、闷痘",
        "bad_for": ["油皮", "痘肌", "油敏肌"]
    },
    "lanolin": {
        "cn_name": "羊毛脂",
        "risk": "medium",
        "desc": "封闭保湿，部分人会过敏、爆闭口",
        "bad_for": ["痘肌", "易闷痘油皮", "羊毛脂过敏人群"]
    },
    "menthol": {
        "cn_name": "薄荷醇",
        "risk": "high",
        "desc": "清凉刺激，扩张血管，加重泛红、灼热",
        "bad_for": ["红血丝肌肤", "敏感肌", "脂溢性皮炎"]
    },
    "citric acid": {
        "cn_name": "柠檬酸",
        "risk": "medium",
        "desc": "果酸类剥脱角质，薄皮容易刺痛干燥",
        "bad_for": ["干敏肌", "屏障受损肌肤"]
    },
    "mineral oil": {
        "cn_name": "矿物油",
        "risk": "medium",
        "desc": "封闭性油脂，油皮长期使用容易闷痘",
        "bad_for": ["油皮", "痘肌"]
    }
}

# 中文成分 → 英文键映射，输入中文也能识别查询
cn_to_en = {
    "乙醇": "alcohol",
    "酒精": "alcohol",
    "香精": "fragrance",
    "水杨酸": "salicylic acid",
    "烟酰胺": "niacinamide",
    "甘油": "glycerin",
    "透明质酸": "hyaluronic acid",
    "玻尿酸": "hyaluronic acid",
    "苯甲醇": "benzyl alcohol",
    "苯氧乙醇": "phenoxyethanol",
    "肉豆蔻酸异丙酯": "isopropyl myristate",
    "羊毛脂": "lanolin",
    "薄荷醇": "menthol",
    "柠檬酸": "citric acid",
    "矿物油": "mineral oil"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    skin_text = ""
    ingredients_input = ""
    skin_select = ""

    if request.method == "POST":
        ingredients_input = request.form.get("ingredients", "")
        skin_select = request.form.get("skin_type", "")
        skin_map = {
            "1": "oily 油皮",
            "2": "dry 干皮",
            "3": "sensitive 敏感肌"
        }
        skin_text = skin_map.get(skin_select, "")
        input_list = [i.strip() for i in ingredients_input.split(",")]
        result = []

        for item in input_list:
            # 区分中文/英文输入，统一匹配库内数据
            if item in cn_to_en:
                en_key = cn_to_en[item]
            else:
                en_key = item.lower()
            if en_key in ingredient_risk:
                result.append(ingredient_risk[en_key])

    return render_template("index.html",
                           result=result,
                           skin_text=skin_text,
                           ingredients_input=ingredients_input,
                           skin_select=skin_select)

if __name__ == "__main__":
    app.run(debug=True)