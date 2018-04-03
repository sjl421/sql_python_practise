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
  - insert(**todo**)
  - insert many
- station(**todo**)
  - create
  - drop
  - insert
  - insert many
- city_aqi(**todo**)
  - create
  - drop
  - insert
  - insert many
- station_aqi(**todo**)
  - create
  - drop
  - insert
  - insert many

## REST API

### city
#### get
获取所有城市数据
```
GET /city
```
获取对应 name 参数的城市数据
```
GET /city?name={city name}
```
#### post
将城市录入数据库 city 表

### station
#### get
获取所有监测站数据
```
GET /station
```
获取对应 station_name 参数的监测站数据
```
GET /station?name={station name}
```
获取对应 station_code 参数的监测站数据
```
GET /station?code={station code}
```
获取对应 city 参数的监测站数据
```
GET /station?city={city}
```
#### post
将监测站录入数据库 station 表

### city_aqi(**todo**)
#### get

#### post

### station_aqi(**todo**)
#### get
#### post
