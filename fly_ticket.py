import concurrent.futures
import json
import threading
import webbrowser
import requests

are_code = "{ '北京':'BJS', '上海':'SHA', '广州':'CAN', '深圳':'SZX', '成都':'CTU', '杭州':'HGH', '武汉':'WUH', '西安':'SIA', '重庆':'CKG', '青岛':'TAO', '长沙':'CSX', '南京':'NKG', '厦门':'XMN', '昆明':'KMG', '大连':'DLC', '天津':'TSN', '郑州':'CGO', '三亚':'SYX', '济南':'TNA', '福州':'FOC', '阿勒泰':'AAT', '阿克苏':'AKU', '鞍山':'AOG', '安庆':'AQG', '安顺':'AVA', '阿拉善左旗':'AXF', '中国澳门':'MFM', '阿里':'NGQ', '阿拉善右旗':'RHT', '阿尔山':'YIE',  '百色':'AEB', '包头':'BAV', '毕节':'BFJ', '北海':'BHY',  '博乐':'BPL', '保山':'BSD', '白城':'DBC', '布尔津':'KJI', '白山':'NBS', '巴彦淖尔':'RLK', '昌都':'BPX', '承德':'CDE', '常德':'CGD', '长春':'CGQ', '朝阳':'CHG', '赤峰':'CIF', '长治':'CIH', '沧源':'CWJ', '常州':'CZX', '池州':'JUH', '大同':'DAT',  '稻城':'DCY', '丹东':'DDG', '迪庆':'DIG', '大理':'DLU', '敦煌':'DNH', '东营':'DOY', '大庆':'DQA', '德令哈':'HXD', '鄂尔多斯':'DSN', '额济纳旗':'EJN', '恩施':'ENH', '二连浩特':'ERL', '阜阳':'FUG', '抚远':'FYJ', '富蕴':'FYN', '果洛':'GMQ', '格尔木':'GOQ',  '固原':'GYU',  '赣州':'KOW', '贵阳':'KWE', '桂林':'KWL', '红原':'AHJ', '海口':'HAK', '河池':'HCJ', '邯郸':'HDG', '黑河':'HEK', '呼和浩特':'HET', '合肥':'HFE', '淮安':'HIA', '怀化':'HJJ', '海拉尔':'HLD', '哈密':'HMI', '衡阳':'HNY', '哈尔滨':'HRB', '和田':'HTN', '花土沟':'HTT', '中国花莲':'HUN', '霍林郭勒':'HUO', '惠州':'HUZ', '黄山':'TXN', '呼伦贝尔':'XRQ', '中国嘉义':'CYI', '景德镇':'JDZ', '加格达奇':'JGD', '嘉峪关':'JGN',  '金昌':'JIC', '九江':'JIU', '荆门':'JM1', '佳木斯':'JMU', '济宁':'JNG', '锦州':'JNZ', '建三江':'JSJ', '鸡西':'JXA', '九寨沟':'JZH',  '揭阳':'SWA', '库车':'KCA', '康定':'KGT', '喀什':'KHG', '凯里':'KJH', '库尔勒':'KRL', '克拉玛依':'KRY', '黎平':'HZH', '澜沧':'JMJ', '龙岩':'LCX', '临汾':'LFQ', '兰州':'LHW', '丽江':'LJG', '荔波':'LLB', '吕梁':'LLV', '临沧':'LNJ', '陇南':'LNL', '六盘水':'LPF', '拉萨':'LXA', '洛阳':'LYA', '连云港':'LYG', '临沂':'LYI', '柳州':'LZH', '泸州':'LZO', '林芝':'LZY', '芒市':'LUM', '牡丹江':'MDG',  '梅州':'MXZ',  '满洲里':'NZH', '漠河':'OHE', '南昌':'KHN', '中国南竿':'LZN', '宁波':'NGB', '宁蒗':'NLH', '南宁':'NNG', '南阳':'NNY', '南通':'NTG', '攀枝花':'PZI', '普洱':'SYM', '琼海':'BAR', '秦皇岛':'BPE', '祁连':'HBQ', '且末':'IQM', '庆阳':'IQN', '黔江':'JIQ', '泉州':'JJN', '衢州':'JUZ', '齐齐哈尔':'NDG', '日照':'RIZ', '日喀则':'RKZ', '若羌':'RQA', '神农架':'HPG', '莎车':'QSZ', '沈阳':'SHE', '石河子':'SHF', '石家庄':'SJW', '上饶':'SQD', '三明':'SQJ', '十堰':'WDS', '邵阳':'WGN', '松原':'YSQ', '台州':'HYN','塔城':'TCG', '腾冲':'TCZ', '铜仁':'TEN', '通辽':'TGO', '天水':'THQ', '吐鲁番':'TLQ', '通化':'TNH', '唐山':'TVS', '太原':'TYN', '五大连池':'DTU', '乌兰浩特':'HLH', '乌兰察布':'UCB', '乌鲁木齐':'URC', '潍坊':'WEF', '威海':'WEH', '文山':'WNH', '温州':'WNZ', '乌海':'WUA', '武夷山':'WUS', '无锡':'WUX', '梧州':'WUZ', '乌拉特中旗':'WZQ', '巫山':'WSK', '兴义':'ACX', '夏河':'GXH', '西双版纳':'JHG', '新源':'NLT', '忻州':'WUT', '信阳':'XAI', '襄阳':'XFN', '西昌':'XIC', '锡林浩特':'XIL', '西宁':'XNN', '徐州':'XUZ', '延安':'ENY', '银川':'INC', '伊春':'LDS', '永州':'LLF', '榆林':'UYN', '运城':'YCU', '宜春':'YIC', '宜昌':'YIH', '伊宁':'YIN', '营口':'YKH', '延吉':'YNJ', '烟台':'YNT', '盐城':'YNZ', '扬州':'YTY', '玉树':'YUS', '岳阳':'YYA', '张家界':'DYG', '舟山':'HSN', '扎兰屯':'NZL', '张掖':'YZY', '昭通':'ZAT', '湛江':'ZHA', '中卫':'ZHY', '张家口':'ZQZ', '珠海':'ZUH', '遵义':'ZYI' }"
are_code = are_code.replace("'","\"")
are_list = json.loads(are_code)
# print(json.dumps(are_list, indent=4, ensure_ascii=False))
# 把 are_list 的key和value对调一下
are_list = dict(zip(are_list.values(), are_list.keys()))
# 获取are_list的key组成一个数组，如果这个key的长度大于三个字符就丢弃掉
cities = [key for key in are_list.keys() if len(key) == 3]


# API接口地址
url = 'https://flights.ctrip.com/itinerary/api/12808/lowestPrice?flightWay=Oneway&dcity={}&acity={}&direct=true&army=false'


def cheapest_cities(range, origin_date, origin_city, target_city):
    if target_city:
        arriving_cities = [target_city]
    else:
        arriving_cities = cities
    # 存储最低票价信息的列表
    cheapest_cities = []

    # 循环发送请求并解析JSON
    for city in arriving_cities:
        targeturl = url.format(origin_city, city)
        print(targeturl)
        response = requests.get(url.format(origin_city,city))
        data = None
        try:
            data = response.json()
        except Exception as e:
            webbrowser.open(targeturl)
            input("Press Enter to continue...")
            response = requests.get(url.format(origin_city, city))
            data = response.json()
        print(data)

        # 检查是否有机票价格信息
        if data and 'data' in data and 'oneWayPrice' in data['data'] and data['data']['oneWayPrice'] is not None:
            for date, price in data['data']['oneWayPrice'][0].items():
                if date == origin_date:
                    cheapest_cities.append((city, price))

    # 按价格从低到高排序
    cheapest_cities.sort(key=lambda x: x[1])
    #print(cheapest_cities)

    # 获取前10个城市
    cheapest_cities = cheapest_cities[:range]
    return dict(cheapest_cities)

def parallel_search(range, origin_date, origin_city, target_city, round2_code_all, round2_all):
    round2 = cheapest_cities(range, origin_date, origin_city, target_city)
    lock.acquire()
    # 把round2的key组成一个数组,并且把这个数组添加到round2_all中,并且去除重复的元素
    round2_code_all.extend(list(round2.keys()))
    round2_code_all = list(set(round2_code_all))
    # 以city_code为key,round2为value,把这个字典添加到round2_all中
    round2_all.append((origin_city, round2))
    lock.release()

if __name__ == '__main__':
    round2_code_all = []
    round2_all = []
    round3_all = {}
    round1 = cheapest_cities(20, '20230429', 'CTU', None)
    print(round1)

    lock = threading.RLock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for city_code, price in round1.items():
            executor.submit(parallel_search, 20, '20230502', city_code, None, round2_code_all, round2_all)

    for city_code in round2_code_all:
        round3 = cheapest_cities(20, '20230504', city_code, 'CTU')
        # 把round3所有元素的key替换成city_code
        round3 = dict(zip([city_code] * len(round3), round3.values()))
        # 把round3放入round3_all中
        round3_all.update(round3)

    # 组合票价
    trip_tuples = []
    for city_code, round2_item in round2_all:
        trip1_price = round1[city_code]
        for city_code2, trip2_price in round2_item.items():
            trip3_price = round3_all.get(city_code2)
            if trip3_price:
                trip_tuples.append((are_list['CTU'] + "-" + are_list[city_code] + "-" + are_list[city_code2] + "-" +
                                    are_list['CTU'], trip1_price, trip2_price, trip3_price,
                                    trip1_price + trip2_price + trip3_price))
    # 按价格从低到高排序
    trip_tuples.sort(key=lambda x: x[4])

    for tuple in trip_tuples:
        print(tuple)

