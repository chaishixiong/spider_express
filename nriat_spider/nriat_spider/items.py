# -*- coding: utf-8 -*-

# Define here the models for your scraped s
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/s.html

import scrapy

class NriatSpider(scrapy.Item):
    pass

class GmWorkItem(scrapy.Item):
    pipeline_level = scrapy.Field()
    source_code = scrapy.Field()
    error_id = scrapy.Field()
    name = scrapy.Field()
    shop_id = scrapy.Field()
    seller_id = scrapy.Field()
    shop_url = scrapy.Field()
    goods_url = scrapy.Field()
    goods_id = scrapy.Field()
    goods_name = scrapy.Field()
    goods_index = scrapy.Field()
    goods_num = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    new_price_value = scrapy.Field()
    price_text = scrapy.Field()
    currency = scrapy.Field()#货币类型
    page_num = scrapy.Field()
    total_num = scrapy.Field()
    average_score = scrapy.Field()
    img_url = scrapy.Field()
    tag = scrapy.Field()
    key = scrapy.Field()
    url = scrapy.Field()
    company_name = scrapy.Field()
    address_detail = scrapy.Field()
    country = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    zip = scrapy.Field()
    contact_people = scrapy.Field()
    good_name = scrapy.Field()
    shop_name = scrapy.Field()
    colour = scrapy.Field()#颜色
    description = scrapy.Field()#商品表述
    delivery = scrapy.Field()#发货地址
    colours = scrapy.Field()#多种颜色
    brand = scrapy.Field()#品牌
    size = scrapy.Field()#产品尺寸
    id = scrapy.Field()
    orders = scrapy.Field()
    media_id = scrapy.Field()
    user_name = scrapy.Field()
    Logistics = scrapy.Field()#w物流后勤
    comment = scrapy.Field()
    comment_num = scrapy.Field()
    comment_distribution = scrapy.Field()#评论分布
    time = scrapy.Field()
    current_page = scrapy.Field()
    comment_score = scrapy.Field()
    stock = scrapy.Field()#库存

    rating_star = scrapy.Field()
    item_status = scrapy.Field()
    show_free_shipping = scrapy.Field()
    json_data = scrapy.Field()

    company = scrapy.Field()
    legal_person = scrapy.Field()
    area = scrapy.Field()

    status = scrapy.Field()
    trade = scrapy.Field()
    type = scrapy.Field()
    aem_count = scrapy.Field()
    tagResult = scrapy.Field()
    Seller = scrapy.Field()
    Since = scrapy.Field()
    last_name = scrapy.Field()
    state = scrapy.Field()
    deep = scrapy.Field()
    sales_money = scrapy.Field()
    sales_num = scrapy.Field()
    company_type = scrapy.Field()
    keep_time = scrapy.Field()
    shop_super = scrapy.Field()
    sort_id = scrapy.Field()
    positive_feedback = scrapy.Field()
    positive_number = scrapy.Field()
    regon = scrapy.Field()
    year = scrapy.Field()
    bad_number = scrapy.Field()
    nip = scrapy.Field()
    company_data = scrapy.Field()
    sort = scrapy.Field()
    sort_second = scrapy.Field()
    score = scrapy.Field()
    score_number = scrapy.Field()
    goodshop_url = scrapy.Field()
    catid = scrapy.Field()
    category = scrapy.Field()
    catid_sub = scrapy.Field()
    category1 = scrapy.Field()
    catid_sub2 = scrapy.Field()
    category2 = scrapy.Field()
    district = scrapy.Field()
    id_s = scrapy.Field()
    categorys = scrapy.Field()
    freight = scrapy.Field()
    inventory = scrapy.Field()
    ean = scrapy.Field()#
    retailer_vrn = scrapy.Field()#
    place = scrapy.Field()
    follower_count = scrapy.Field()
    rating_good = scrapy.Field()
    rating_bad = scrapy.Field()
    cancellation_rate = scrapy.Field()
    location = scrapy.Field()
    view_count = scrapy.Field()
    item_count = scrapy.Field()
    shop_location = scrapy.Field()
    anchor_id = scrapy.Field()
    nick = scrapy.Field()
    fans_count = scrapy.Field()
    follow_count = scrapy.Field()
    live_count = scrapy.Field()
    live_id = scrapy.Field()
    live_time = scrapy.Field()
    viewer_total = scrapy.Field()
    viewer_count = scrapy.Field()
    live_info = scrapy.Field()
    cid = scrapy.Field()
    match_id = scrapy.Field()
    page = scrapy.Field()
    fruugo_id = scrapy.Field()
    up_id = scrapy.Field()
    rid = scrapy.Field()
    c2name = scrapy.Field()
    ol = scrapy.Field()
    video = scrapy.Field()
    plays = scrapy.Field()
    fans = scrapy.Field()
    signature = scrapy.Field()
    labels = scrapy.Field()
    gift_num = scrapy.Field()
    getgift_num = scrapy.Field()
    pinyin = scrapy.Field()
    hotel_num = scrapy.Field()
    hotel_id = scrapy.Field()
    hotel_name = scrapy.Field()
    hotel_enname = scrapy.Field()
    loupan_id = scrapy.Field()
    id_lou = scrapy.Field()
    lou_name = scrapy.Field()
    miaoshu = scrapy.Field()
    loucheng = scrapy.Field()
    mianji = scrapy.Field()
    city_info = scrapy.Field()
    danjia = scrapy.Field()
    huxing = scrapy.Field()
    type_lou = scrapy.Field()
    open_time = scrapy.Field()
    name1 = scrapy.Field()
    id_city = scrapy.Field()
    pinyin_city = scrapy.Field()
    area_name = scrapy.Field()
    area_url = scrapy.Field()
    house_url = scrapy.Field()
    house_id = scrapy.Field()
    color = scrapy.Field()
    age = scrapy.Field()
    city_shopnum = scrapy.Field()
    branch_name = scrapy.Field()
    star_score = scrapy.Field()
    review_count = scrapy.Field()
    region_name = scrapy.Field()
    category_name = scrapy.Field()
    dish_tags = scrapy.Field()
    has_takeaway = scrapy.Field()
    city_name = scrapy.Field()
    cate_name = scrapy.Field()
    shop_about = scrapy.Field()
    vender_id = scrapy.Field()
    promo_statu = scrapy.Field()
    sales_vague = scrapy.Field()
    room_name = scrapy.Field()
    labelx = scrapy.Field()
    labely = scrapy.Field()
    summary = scrapy.Field()
    county = scrapy.Field()
    town = scrapy.Field()

    good_id = scrapy.Field()
    good_url = scrapy.Field()
    sales = scrapy.Field()
    ratingCountLabel = scrapy.Field()
    huobi_type = scrapy.Field()

    phone = scrapy.Field()
    email = scrapy.Field()
    company_info = scrapy.Field()
    country_w = scrapy.Field()
    country_p = scrapy.Field()
    order = scrapy.Field()
    qq = scrapy.Field()
    line = scrapy.Field()
    list_con = scrapy.Field()
    company_img = scrapy.Field()
    warehouse_img = scrapy.Field()
    date = scrapy.Field()

    main_sales = scrapy.Field()
    fax = scrapy.Field()
    creat_date = scrapy.Field()
    start_date = scrapy.Field()
    general_manager = scrapy.Field()
    registered_capital = scrapy.Field()
    share_capital = scrapy.Field()
    circulating_shares = scrapy.Field()
    plate = scrapy.Field()
    summaryPrice = scrapy.Field()
    winningSupplierName = scrapy.Field()
    purchaser = scrapy.Field()


class AmazonItem(scrapy.Item):
    url = scrapy.Field()
    good_name = scrapy.Field()
    level = scrapy.Field()
    evaluates = scrapy.Field()
    price = scrapy.Field()
    catelog_name = scrapy.Field()
    catelog_url = scrapy.Field()
    deep = scrapy.Field()
    offer_from = scrapy.Field()
    goodid = scrapy.Field()



class softtime(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    NodeId = scrapy.Field()
    name = scrapy.Field()
    SaleCount = scrapy.Field()
    BrandCount = scrapy.Field()
    Url = scrapy.Field()
    totalsalecount = scrapy.Field()
    Id = scrapy.Field()
    ASIN = scrapy.Field()
    Name = scrapy.Field()
    NameEncode = scrapy.Field()
    Brand = scrapy.Field()
    BrandEncode = scrapy.Field()
    ImageEncode = scrapy.Field()
    Store = scrapy.Field()
    Rank = scrapy.Field()
    Solder = scrapy.Field()
    CommentCount = scrapy.Field()
    SaleTime = scrapy.Field()
    Score = scrapy.Field()
    Variants = scrapy.Field()
    OtherSellerCount = scrapy.Field()
    EBC = scrapy.Field()
    CurrentSalePrice = scrapy.Field()
    SalePrice = scrapy.Field()
    PromotionRecords = scrapy.Field()
    PotentialEvaluation = scrapy.Field()
    Income = scrapy.Field()
    FBAFee = scrapy.Field()
    BestSeller = scrapy.Field()
    ListingHeight = scrapy.Field()
    ListingWidth = scrapy.Field()
    ListingDepath = scrapy.Field()
    SizeStr = scrapy.Field()
    ShippingWeight = scrapy.Field()
    PickAndPack = scrapy.Field()
    Referral = scrapy.Field()
    Storage = scrapy.Field()
    Deliver = scrapy.Field()
    ReferralRate = scrapy.Field()
    TypeName = scrapy.Field()
    Image = scrapy.Field()
    BrandSalePercent = scrapy.Field()
    TotalSalePercent = scrapy.Field()
    BDCount = scrapy.Field()
    Coupon = scrapy.Field()
    CouponRecord = scrapy.Field()
    ActualSalePrice = scrapy.Field()
    Volume = scrapy.Field()
    Productsize = scrapy.Field()
    error_id = scrapy.Field()
    key = scrapy.Field()
    source_code = scrapy.Field()

class taobao(scrapy.Item):
    zhuangtai = scrapy.Field()
    selllerid = scrapy.Field()
    shop_id = scrapy.Field()
    zhanggui = scrapy.Field()
    nickurl = scrapy.Field()
    nick = scrapy.Field()
    shop_name = scrapy.Field()
    haoping = scrapy.Field()
    miaoshuxf = scrapy.Field()
    fuwutd = scrapy.Field()
    fahuosd = scrapy.Field()
    area = scrapy.Field()
    phone = scrapy.Field()
    shopurl = scrapy.Field()
    pipeline_level = scrapy.Field()
    _id = scrapy.Field()
    _name = scrapy.Field()
    price = scrapy.Field()
    mouth_count = scrapy.Field()
    biuaoshi = scrapy.Field()
    gongsibs = scrapy.Field()
    seller_id = scrapy.Field()
    company_name = scrapy.Field()
    pingfeng = scrapy.Field()
    miaoshu = scrapy.Field()
    fuwu = scrapy.Field()
    wuliu = scrapy.Field()
    seller_name = scrapy.Field()
    baozhengjin = scrapy.Field()
    lianxifanshi = scrapy.Field()
    zhutibg = scrapy.Field()
    cate_id = scrapy.Field()
    zjprice = scrapy.Field()
    fzjprice = scrapy.Field()
    dizhi = scrapy.Field()
    xiaoliang = scrapy.Field()
    taobao_shop_name = scrapy.Field()
    taobao_seller_name = scrapy.Field()
    taobao__id = scrapy.Field()
    taobao_cate_id = scrapy.Field()
    taobao_cateroot_id = scrapy.Field()
    shangjiatime = scrapy.Field()
    shop_type = scrapy.Field()
    taobao_shop_dizhi = scrapy.Field()
    taobao_price = scrapy.Field()
    tmall_shop_name = scrapy.Field()
    tmall_selller_name = scrapy.Field()
    tmall_shop_dizhi = scrapy.Field()
    tamall_goods_name = scrapy.Field()
    tmall_cate_id = scrapy.Field()
    tmall_brand = scrapy.Field()
    tmall_price = scrapy.Field()
    tmall_shop_type = scrapy.Field()
    shop_url = scrapy.Field()
    kaidiantime = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    shoucang = scrapy.Field()
    shoucang2 = scrapy.Field()
    tellphone_s = scrapy.Field()
    fenphone = scrapy.Field()
    brand = scrapy.Field()
    tupiao = scrapy.Field()
    shop_typeloge = scrapy.Field()
    beijin = scrapy.Field()
    shop_dj = scrapy.Field()
    shop_nl = scrapy.Field()
    wufu = scrapy.Field()
    hywuliu = scrapy.Field()
    hymiaoshu = scrapy.Field()
    hywufu = scrapy.Field()
    shangping = scrapy.Field()
    shangxing = scrapy.Field()
    wangwang = scrapy.Field()
    gongshang_id = scrapy.Field()
    main_sale_id = scrapy.Field()
    miaoshu_pf_s = scrapy.Field()
    fuwu_pf_s = scrapy.Field()
    wuliu_pf_s = scrapy.Field()
    biaoshi = scrapy.Field()
    xid = scrapy.Field()
    v_id = scrapy.Field()
    nv_id = scrapy.Field()
    miaoshu_ufb = scrapy.Field()
    miaoshu_th = scrapy.Field()
    fuwu_ufb = scrapy.Field()
    fuwu_th = scrapy.Field()
    wuliu_ufb = scrapy.Field()
    wuliu_th = scrapy.Field()
    shop_haoping = scrapy.Field()
    seller_xinyong = scrapy.Field()
    good_name = scrapy.Field()
    promotion_price = scrapy.Field()
    sell_count = scrapy.Field()
    quantity = scrapy.Field()
    favor_count = scrapy.Field()
    brand_id = scrapy.Field()
    category_id = scrapy.Field()
    category_id_lv1 = scrapy.Field()
    sub__name = scrapy.Field()
    pic = scrapy.Field()
    shop_id_key = scrapy.Field()
    source_code = scrapy.Field()


class EbayItemGood(scrapy.Item):
    good_id = scrapy.Field()
    good_name = scrapy.Field()
    price_dollar = scrapy.Field()
    price_RMB = scrapy.Field()
    project_location = scrapy.Field()
    brand = scrapy.Field()
    seller_name = scrapy.Field()
    sales_count = scrapy.Field()
    cat_1 = scrapy.Field()
    cat_2 = scrapy.Field()
    cat_3 = scrapy.Field()
    cat_4 = scrapy.Field()
    cat_5 = scrapy.Field()
    cat_6 = scrapy.Field()
    source_code = scrapy.Field()

class LinioItem(scrapy.Item):
    shop_name = scrapy.Field()
    good_id = scrapy.Field()
    good_name = scrapy.Field()
    brand = scrapy.Field()
    good_score = scrapy.Field()

    price = scrapy.Field()
    comment = scrapy.Field()
    good_url = scrapy.Field()
    source_code = scrapy.Field()

    cat1 = scrapy.Field()
    cat2 = scrapy.Field()
    cat3 = scrapy.Field()
    cat4 = scrapy.Field()
    shop_score = scrapy.Field()
    shop_url = scrapy.Field()
    pipeline_level = scrapy.Field()

class Ozon1Item(scrapy.Item):
    shop_id = scrapy.Field()
    good_name = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    discount = scrapy.Field()
    leibie = scrapy.Field()
    comment_nums = scrapy.Field()
    source_code = scrapy.Field()

class KilimallItem(scrapy.Item):
    comment_nums = scrapy.Field()
    source_code = scrapy.Field()
    goods_id = scrapy.Field()
    good_name = scrapy.Field()
    new_price = scrapy.Field()
    old_price = scrapy.Field()
    shop_name = scrapy.Field()
    score = scrapy.Field()
