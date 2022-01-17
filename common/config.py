from configparser import RawConfigParser  # 配置解析器


def conf(sections):
    cfg = RawConfigParser()
    cfg.read('../Conf/config.ini', encoding='UTF-8')
    return dict(cfg.items(sections))
