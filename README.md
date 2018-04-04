# Python + MySQL 练手项目

> 之前一直没有接触过使用纯 MySQL 语句的项目，基本都是用 ORM，本项目为刚入门 MySQL 而生，简单易懂，旨在更清晰的学习 MySQL。

## 文件结构

- data 数据库基础数据，取全国某一天的空气质量数据
  - all_cities.json 所有城市的空气质量数据
  - aqi_ranking.json 所有城市监测站的空气质量数据
  - querys.json 所有城市数据
  - station_names.json 所有城市监测站数据

- handler Web Service 接口
  - base.py 接口基类
  - city.py 城市接口
  - station.py 监测站接口

- db 数据库操作接口
  - base.py 基本数据库操作
  - city.py 城市数据库操作
  - station.py 监测站数据库操作

- web.py Web Service 入口

- config.py 配置文件，包含数据库配置信息

## 表

- city
  - create
  - drop
  - insert
  - insert many
  - select
- station
  - create
  - drop
  - insert
  - insert many
  - select
- city_aqi
  - create
  - drop
  - insert
  - insert many
  - select
- station_aqi
  - create
  - drop
  - insert
  - insert many
  - select

## REST API

### city
#### get
获取所有城市数据
```
GET /city
```

```
{
    "status": "success",
    "count": 375,
    "data": [
        [
            1,
            "七台河"
        ],
        ...,
        [
            2,
            "三亚"
        ]
    ]
}
```
获取对应 name 参数的城市数据
```
GET /city?name={city name}
```

```
{
    "status": "success",
    "count": 1,
    "data": [
        [
            47,
            "北京"
        ]
    ]
}
```
#### post
将城市录入数据库 city 表
```
POST /city
```
### station
#### get
获取所有监测站数据
```
GET /station
```

```
{
    "status": "success",
    "count": 1628,
    "data": [
        [
            1122,
            "新建　",
            "2261A",
            "七台河"
        ],
        ..,
        [
            1121,
            "环保局",
            "2260A",
            "七台河"
        ]
    ]
}
```
获取对应 name 参数的监测站数据
```
GET /station?name={station name}
```

```
{
    "status": "success",
    "count": 15,
    "data": [
        [
            1121,
            "环保局",
            "2260A",
            "七台河"
        ],
        ...,
        [
            57,
            "环保局",
            "1047A",
            "邯郸"
        ]
    ]
}
```
获取对应 code 参数的监测站数据
```
GET /station?code={station code}
```

```
{
    "status": "success",
    "count": 1,
    "data": [
        [
            1121,
            "环保局",
            "2260A",
            "七台河"
        ]
    ]
}
```
获取对应 city 参数的监测站数据
```
GET /station?city={city}
```

```
{
    "status": "success",
    "count": 23,
    "data": [
        [
            34,
            " 淮河道",
            "1019A"
        ],
        ...,
        [
            23,
            "跃进路",
            "1021A"
        ]
    ]
}
```
#### post
将监测站录入数据库 station 表
```
POST /station
```

### city_aqi
#### get
获取所有城市空气质量数据
```
GET /aqi/city
```
```
{
    "status": "success",
    "count": 372,
    "data": [
        {
            "aqi": 18,
            "area": "林芝地区",
            "co": 0.35,
            "co_24h": 0.35,
            "no2": 6,
            "no2_24h": 7,
            "o3": 51,
            "o3_24h": 57,
            "o3_8h": 35,
            "o3_8h_24h": 36,
            "pm10": 16,
            "pm10_24h": 20,
            "pm2_5": 4,
            "pm2_5_24h": 4,
            "quality": "",
            "level": "优",
            "so2": "一级",
            "so2_24h": 3,
            "primary_pollutant": 3,
            "time_point": "2017-08-16 16:00:00"
        },
        ...,
        {
            "aqi": 29,
            "area": "日喀则地区",
            "co": 0.35,
            "co_24h": 0.45,
            "no2": 2,
            "no2_24h": 11,
            "o3": 68,
            "o3_24h": 77,
            "o3_8h": 56,
            "o3_8h_24h": 56,
            "pm10": 27,
            "pm10_24h": 31,
            "pm2_5": 6,
            "pm2_5_24h": 9,
            "quality": "",
            "level": "优",
            "so2": "一级",
            "so2_24h": 5,
            "primary_pollutant": 5,
            "time_point": "2017-08-16 16:00:00"
        }
    ]
}
```
获取对应 name、code、city 城市空气质量数据
```
GET /aqi/city?name={city}
```
```
{
    "status": "success",
    "count": 1,
    "data": [
        {
            "aqi": 292,
            "area": "北京",
            "co": 2.058,
            "co_24h": 1.7,
            "no2": 72,
            "no2_24h": 71,
            "o3": 149,
            "o3_24h": 193,
            "o3_8h": 148,
            "o3_8h_24h": 148,
            "pm10": 265,
            "pm10_24h": 222,
            "pm2_5": 241,
            "pm2_5_24h": 224,
            "quality": "颗粒物(PM2.5)",
            "level": "重度污染",
            "so2": "五级",
            "so2_24h": 10,
            "primary_pollutant": 10,
            "time_point": "2018-04-02 19:00:00"
        }
    ]
}
```
#### post
将城市空气质量录入数据库 city_aqi 表
```
POST /aqi/city
```

### station_aqi
#### get
获取所有监测站空气质量数据
```
GET /aqi/station
```
```
{
    "status": "success",
    "count": 1628,
    "data": [
        {
            "aqi": 288,
            "area": "北京",
            "co": 2.1,
            "co_24h": 1.7,
            "no2": 65,
            "no2_24h": 74,
            "o3": 133,
            "o3_24h": 179,
            "o3_8h": 130,
            "o3_8h_24h": 130,
            "pm10": 257,
            "pm10_24h": 240,
            "pm2_5": 238,
            "pm2_5_24h": 209,
            "position_name": "万寿西宫",
            "primary_pollutant": "细颗粒物(PM2.5)",
            "quality": "重度污染",
            "so2": 10,
            "so2_24h": 11,
            "time_point": "2018-04-02 19:00:00"
        },
        ...,
        {
            "aqi": 277,
            "area": "北京",
            "co": 1.8,
            "co_24h": 1.5,
            "no2": 72,
            "no2_24h": 57,
            "o3": 167,
            "o3_24h": 213,
            "o3_8h": 166,
            "o3_8h_24h": 166,
            "pm10": 0,
            "pm10_24h": 162,
            "pm2_5": 227,
            "pm2_5_24h": 218,
            "position_name": "定陵",
            "primary_pollutant": "细颗粒物(PM2.5)",
            "quality": "重度污染",
            "so2": 9,
            "so2_24h": 8,
            "time_point": "2018-04-02 19:00:00"
        }
    ]
}
```
获取对应 city 的监测站空气质量数据
```
GET /aqi/station?name={city name}
```
```
{
    "status": "success",
    "count": 12,
    "data": [
        {
            "aqi": 288,
            "area": "北京",
            "co": 2.1,
            "co_24h": 1.7,
            "no2": 65,
            "no2_24h": 74,
            "o3": 133,
            "o3_24h": 179,
            "o3_8h": 130,
            "o3_8h_24h": 130,
            "pm10": 257,
            "pm10_24h": 240,
            "pm2_5": 238,
            "pm2_5_24h": 209,
            "position_name": "万寿西宫",
            "primary_pollutant": "细颗粒物(PM2.5)",
            "quality": "重度污染",
            "so2": 10,
            "so2_24h": 11,
            "time_point": "2018-04-02 19:00:00"
        },
        ...,
        {
            "aqi": 277,
            "area": "北京",
            "co": 1.8,
            "co_24h": 1.5,
            "no2": 72,
            "no2_24h": 57,
            "o3": 167,
            "o3_24h": 213,
            "o3_8h": 166,
            "o3_8h_24h": 166,
            "pm10": 0,
            "pm10_24h": 162,
            "pm2_5": 227,
            "pm2_5_24h": 218,
            "position_name": "定陵",
            "primary_pollutant": "细颗粒物(PM2.5)",
            "quality": "重度污染",
            "so2": 9,
            "so2_24h": 8,
            "time_point": "2018-04-02 19:00:00"
        }
    ]
}
```
#### post
将监测站空气质量录入数据库 station_aqi 表
```
POST /aqi/station
```