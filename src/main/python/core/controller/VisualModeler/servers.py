# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/13 下午5:49


from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.core.app.VisualModeler.process.draw.processInfo import Process
from src.main.python.core.app.VisualModeler.process.draw.drawAction import DrawProcess
from src.main.python.core.app.VisualModeler.process.draw.manualExec import ManualExecute
from src.main.python.core.app.VisualModeler.process.node.business.reportDashboard import ReportDashboard
from src.main.python.core.app.VisualModeler.commonInfo.template import Template, ZgDataManage, DoubleConfirm
from src.main.python.core.app.VisualModeler.commonInfo.proxy import Proxy
from src.main.python.core.app.VisualModeler.commonInfo.field import ProfessionField
from src.main.python.core.app.VisualModeler.commonInfo.database import Database
from src.main.python.core.app.VisualModeler.commonInfo.database import TableManagement
from src.main.python.core.app.VisualModeler.commonInfo.script import Script
from src.main.python.core.app.VisualModeler.commonInfo.ai import AiModel
from src.main.python.core.app.VisualModeler.commonInfo.mailbox import Mail
from src.main.python.core.app.VisualModeler.commonInfo.ftp import FTP
from src.main.python.core.app.VisualModeler.commonInfo.system import ThirdSystem
from src.main.python.core.app.VisualModeler.commonInfo.interface import Interface
from src.main.python.core.app.VisualModeler.commonInfo.file import File
from src.main.python.core.app.VisualModeler.cmd.cmdSet import CmdSet
from src.main.python.core.app.VisualModeler.cmd.cmdTpl import CmdTemplate
from src.main.python.core.app.VisualModeler.cmd.relurX import RulerX
from src.main.python.core.app.VisualModeler.cmd.regexpTpl import RegexpTemplate
from src.main.python.core.app.VisualModeler.edata.eDataTpl import EDataTemplate
from src.main.python.core.app.VisualModeler.personal.myMonitor import Monitor
from src.main.python.core.app.VisualModeler.task.taskManage import TaskManage
# from src.main.python.lib.autoLogin import auto_enter_vm
from src.main.python.lib.wrap import Wrap
from src.main.python.lib.logger import log


@Wrap(wrap_func='auto_enter_vm')
def actions(func, param):

    run_flag = True

    if func == "ChooseMenu":
        action = DoctorWho()
        action.choose_menu(menu_path=param.get("菜单"))

    # 流程配置
    elif func == "AddProcess":
        action = Process()
        action.add(process_name=param.get("流程名称"), field=param.get("专业领域"), process_type=param.get("流程类型"),
                   exec_mode=param.get("执行模式"), process_desc=param.get("流程说明"), advance_set=param.get("高级配置"))

    elif func == "UpdateProcess":
        action = Process()
        update_map = param.get("修改内容")
        action.update(process=param.get("流程名称"), process_name=update_map.get("流程名称"), field=update_map.get("专业领域"),
                      exec_mode=update_map.get("执行模式"), process_desc=update_map.get("流程说明"),
                      advance_set=update_map.get("高级配置"))

    elif func == "DeleteProcess":
        action = Process()
        action.delete(process_name=param.get("流程名称"))

    elif func == "CopyProcess":
        action = Process()
        action.copy(process_name=param.get("流程名称"), main_process_name=param.get("主流程名称"),
                    sub_process_name_list=param.get("子流程名称列表"))

    elif func == "ProcessDataClear":
        action = Process()
        action.data_clear(process_name=param.get("流程名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListProcess":
        action = Process()
        action.search(query=param.get("查询条件"))

    elif func == "AddNode":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.locate_node(node_type=param.get("节点类型"), x_loc=param.get("左边距"), y_loc=param.get("上边距"))

    elif func == "SetEndNode":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.set_end_node(status=param.get("状态"))

    elif func == "NodeBusinessConf":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.node_business_conf(node_type=param.get("节点类型"), node_name=param.get("节点名称"), **param.get("业务配置"))

    elif func == "NodeFetchConf":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.node_fetch_conf(node_type=param.get("节点类型"), node_name=param.get("节点名称"), **param.get("取数配置"))

    elif func == "NodeControlConf":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.node_control_conf(node_type=param.get("节点类型"), node_name=param.get("节点名称"), **param.get("控制配置"))

    elif func == "NodeOptConf":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.node_operate_conf(node_type=param.get("节点类型"), node_name=param.get("节点名称"), array=param.get("操作配置"))

    elif func == "LineNode":
        action = DrawProcess(process_name=param.get("流程名称"))
        action.combine(source_node_name=param.get("起始节点名称"), target_node_name=param.get("终止节点名称"),
                       logic=param.get("关联关系"))

    elif func == "TestProcess":
        action = ManualExecute(process_name=param.get("流程名称"))
        action.test()

    elif func == "FastRunProcess":
        action = ManualExecute(process_name=param.get("流程名称"))
        action.fast_run(params=param.get("参数列表"))

    elif func == "UpdateProcessStatus":
        action = Process()
        action.set_status(process_name=param.get("流程名称"), process_status=param.get("状态"))

    elif func == "ProcessApproval":
        action = Process()
        action.approval(process_name=param.get("流程名称"))

    elif func == "CreateProcessTask":
        action = Process()
        action.create_task(process_name=param.get("流程名称"), task_info=param.get("任务配置"))

    # 报表节点仪表盘配置
    elif func == "AccessReportDashboard":
        action = ReportDashboard()
        action.access_report_dashboard(process_name=param.get("流程名称"), node_name=param.get("节点名称"))

    elif func == "DashboardConf":
        action = ReportDashboard()
        action.set_dashboard(dashboard_info=param.get("仪表盘配置"))

    elif func == "DashboardImageConf":
        action = ReportDashboard()
        action.set_image(image=param.get("图像配置"))

    elif func == "DashboardImageClear":
        action = ReportDashboard()
        action.clear_image(image_name=param.get("图像名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "DashboardAddImage":
        action = ReportDashboard()
        action.add_in_image(image_list=param.get("图像列表"))

    elif func == "DashboardDictAdd":
        action = ReportDashboard()
        action.add_dictionary(dictionary_list=param.get("字典配置"))

    elif func == "DashboardDictClear":
        action = ReportDashboard()
        action.clear_dictionary(dictionary_name=param.get("字典名称"), fuzzy_match=param.get("模糊匹配"))

    # 网元模版配置
    elif func == "AddZgTemp":
        action = Template(temp_type=param.get("模版类型"))
        action.add_zg_temp(zg_temp_name=param.get("模版名称"))

    elif func == "UpdateZgTemp":
        action = Template(temp_type=param.get("模版类型"))
        update_map = param.get("修改内容")
        action.update_zg_temp(zg_temp=param.get("模版名称"), zg_temp_name=update_map.get("新模版名称"))

    elif func == "SaveZgTempCol":
        action = Template(temp_type=param.get("模版类型"))
        action.col_sets(zg_temp_name=param.get("模版名称"), col_set=param.get("列配置"))

    elif func == "UpdateColSearch":
        action = Template(temp_type=param.get("模版类型"))
        action.set_search(zg_temp_name=param.get("模版名称"), col_list=param.get("列名列表"))

    elif func == "UpdateColNull":
        action = Template(temp_type=param.get("模版类型"))
        action.set_null(zg_temp_name=param.get("模版名称"), col_list=param.get("列名列表"))

    elif func == "UpdateColFrozen":
        action = Template(temp_type=param.get("模版类型"))
        action.set_frozen(zg_temp_name=param.get("模版名称"), col_list=param.get("列名列表"))

    elif func == "DeleteZgTemp":
        action = Template(temp_type=param.get("模版类型"))
        action.delete_zg_temp(zg_temp_name=param.get("模版名称"))

    elif func == "CopyZgTemp":
        action = Template(temp_type=param.get("模版类型"))
        action.copy_zg_temp(zg_temp_name=param.get("模版名称"), copy_name=param.get("新模版名称"))

    elif func == "ZgTempPushAlarm":
        action = Template(temp_type=param.get("模版类型"))
        action.push_alarm(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempSyncAlarm":
        action = Template(temp_type=param.get("模版类型"))
        action.sync_alarm(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempRevokeAlarm":
        action = Template(temp_type=param.get("模版类型"))
        action.revoke_alarm(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempPushDashboard":
        action = Template(temp_type=param.get("模版类型"))
        action.push_dashboard(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempSyncDashboard":
        action = Template(temp_type=param.get("模版类型"))
        action.sync_dashboard(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempRevokeDashboard":
        action = Template(temp_type=param.get("模版类型"))
        action.revoke_dashboard(zg_temp_name=param.get("模版名称"))

    elif func == "ZgTempDataClear":
        action = Template(temp_type=param.get("模版类型"))
        action.data_clear(zg_temp_name=param.get("模版名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListZgTemp":
        action = Template(temp_type=param.get("模版类型"))
        action.search(query=param.get("查询条件"))

    elif func == "ZgAddData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.add_data(data_info=param.get("数据信息"))

    elif func == "ZgUpdateData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.update_data(netunit_name=param.get("网元名称"), data_info=param.get("数据信息"))

    elif func == "ZgListData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.search_data(query=param.get("查询条件"))

    elif func == "ZgDeleteData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.delete_data(query=param.get("查询条件"))

    elif func == "ZgUploadData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.upload(file_path=param.get("文件路径"))

    elif func == "ZgDownloadTempl":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.download_templ()

    elif func == "ZgExportData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.export()

    elif func == "ZgClearData":
        action = ZgDataManage(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.clear()

    elif func == "ZgDataConfirmListData":
        action = DoubleConfirm(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.search_data(query=param.get("查询条件"))

    elif func == "ZgDataConfirmSelected":
        action = DoubleConfirm(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.confirm_selected(ne_list=param.get("网元列表"), query=param.get("查询条件"))

    elif func == "ZgDataConfirmAll":
        action = DoubleConfirm(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.confirm_all(query=param.get("查询条件"))

    elif func == "ZgDataRevokeSelected":
        action = DoubleConfirm(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.revoke_selected(ne_list=param.get("网元列表"), query=param.get("查询条件"))

    elif func == "ZgDataRevokeAll":
        action = DoubleConfirm(temp_type=param.get("模版类型"), zg_temp_name=param.get("模版名称"))
        action.revoke_all(query=param.get("查询条件"))

    # 代理管理
    elif func == "AddProxy":
        action = Proxy()
        action.add(proxy_name=param.get("代理名称"), ip=param.get("代理服务器"), port=param.get("代理端口"),
                   username=param.get("代理用户名"), pwd=param.get("代理密码"), protocol=param.get("代理协议"),
                   enable=param.get("是否有效"), data_type=param.get("数据类型"))

    elif func == "UpdateProxy":
        action = Proxy()
        update_map = param.get("修改内容")
        action.update(proxy=param.get("代理名称"), proxy_name=update_map.get("代理名称"), ip=update_map.get("代理服务器"),
                      port=update_map.get("代理端口"), username=update_map.get("代理用户名"), pwd=update_map.get("代理密码"),
                      protocol=update_map.get("代理协议"), enable=update_map.get("是否有效"),
                      data_type=update_map.get("数据类型"))

    elif func == "DeleteProxy":
        action = Proxy()
        action.delete(proxy_name=param.get("代理名称"))

    elif func == "ProxyDataClear":
        action = Proxy()
        action.data_clear(proxy_name=param.get("代理名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListProxy":
        action = Proxy()
        action.search(query=param.get("查询条件"))

    # 专业领域管理
    elif func == "AddField":
        action = ProfessionField()
        action.add(field_name=param.get("专业领域名称"))

    elif func == "UpdateField":
        action = ProfessionField()
        update_map = param.get("修改内容")
        action.update(field=param.get("专业领域名称"), field_name=update_map.get("专业领域名称"))

    elif func == "DeleteField":
        action = ProfessionField()
        action.delete(field_name=param.get("专业领域名称"))

    elif func == "FieldDataClear":
        action = ProfessionField()
        action.data_clear(field_name=param.get("专业领域名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListField":
        action = ProfessionField()
        action.search(query=param.get("查询条件"))

    # 数据库管理
    elif func == "AddDatabase":
        action = Database()
        action.add(db_name=param.get("数据库名称"), db_driver=param.get("数据库驱动"), db_url=param.get("数据库URL"),
                   username=param.get("用户名"), pwd=param.get("密码"), belong_type=param.get("归属类型"),
                   data_type=param.get("数据类型"))

    elif func == "UpdateDatabase":
        action = Database()
        update_map = param.get("修改内容")
        action.update(db=param.get("数据库名称"), db_name=update_map.get("数据库名称"), db_driver=update_map.get("数据库驱动"),
                      db_url=update_map.get("数据库URL"), username=update_map.get("用户名"), pwd=update_map.get("密码"),
                      belong_type=update_map.get("归属类型"), data_type=update_map.get("数据类型"))

    elif func == "TestDatabase":
        action = Database()
        action.test(db_name=param.get("数据库名称"))

    elif func == "DeleteDatabase":
        action = Database()
        action.delete(db_name=param.get("数据库名称"))

    elif func == "DBDataClear":
        action = Database()
        action.data_clear(db_name=param.get("数据库名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListDatabase":
        action = Database()
        action.search(query=param.get("查询条件"))

    # 数据库管理的数据管理
    elif func == "AddDBTable":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.add_table(zh_name=param.get("数据表名称"), en_name=param.get("表英文名"))

    elif func == "DeleteDBTable":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.delete_table(zh_name=param.get("数据表名称"))

    elif func == "AddDBTableCol":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.add_cols(zh_name=param.get("数据表名称"), cols=param.get("列信息"))

    elif func == "EditDBTableCol":
        action = TableManagement(database_name=param.get("数据库名称"))
        update_map = param.get("修改内容")
        action.edit_col(zh_name=param.get("数据表名称"), obj_col=param.get("列名(自定义)"),
                        col_info=update_map.get("列信息"))

    elif func == "DeleteDBTableCol":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.delete_col(zh_name=param.get("数据表名称"), zh_col_name=param.get("列名(自定义)"))

    elif func == "ImportDBTable":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.import_table(zh_name=param.get("数据表名称"), en_name=param.get("表英文名"),
                            col_file_name=param.get("字段文件名"))

    elif func == "DBTableClear":
        action = TableManagement(database_name=param.get("数据库名称"))
        action.data_clear(zh_name=param.get("数据表名称"), fuzzy_match=param.get("模糊匹配"))

    # 脚本管理
    elif func == "AddScript":
        action = Script()
        action.add(script_name=param.get("脚本名称"), script_type=param.get("脚本类型"), data_type=param.get("数据类型"))

    elif func == "UpdateScript":
        action = Script()
        update_map = param.get("修改内容")
        action.update(script=param.get("脚本名称"), script_name=update_map.get("脚本名称"),
                      data_type=update_map.get("数据类型"))

    elif func == "SaveScriptVersion":
        action = Script()
        action.choose_version(script_name=param.get("脚本名称"), ver_no=param.get("版本号"))
        action.save_current_version()

    elif func == "SaveNewScriptVersion":
        action = Script()
        action.choose_version(script_name=param.get("脚本名称"), ver_no=param.get("版本号"))
        action.save_new_version()

    elif func == "AddScriptParams":
        action = Script()
        action.add_param(script_name=param.get("脚本名称"), ver_no=param.get("版本号"), params=param.get("脚本参数"))

    elif func == "UpdateScriptParams":
        action = Script()
        action.update_param(script_name=param.get("脚本名称"), ver_no=param.get("版本号"), params=param.get("脚本参数"))

    elif func == "DownloadScriptVersion":
        action = Script()
        action.download_version(script_name=param.get("脚本名称"), ver_no=param.get("版本号"))

    elif func == "DeleteScriptVersion":
        action = Script()
        action.delete_version(script_name=param.get("脚本名称"), ver_no=param.get("版本号"))

    elif func == "SubmitScriptApproval":
        action = Script()
        action.submit_for_approval(script_name=param.get("脚本名称"), ver_no=param.get("版本号"))

    elif func == "UploadScriptFile":
        action = Script()
        action.upload_script_file(script_name=param.get("脚本名称"), ver_no=param.get("版本号"), file_name=param.get("脚本文件名"))

    elif func == "ScriptFileRClick":
        action = Script()
        action.script_file_r_click(script_name=param.get("脚本名称"), ver_no=param.get("版本号"), file_name=param.get("脚本文件名"),
                                   operate=param.get("右键"))

    elif func == "UpdateScriptFileContent":
        action = Script()
        action.update_script_content(script_name=param.get("脚本名称"), ver_no=param.get("版本号"), file_name=param.get("脚本文件名"),
                                     content=param.get("脚本内容"))

    elif func == "DeleteScript":
        action = Script()
        action.delete(script_name=param.get("脚本名称"))

    elif func == "ScriptDataClear":
        action = Script()
        action.data_clear(script_name=param.get("脚本名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListScript":
        action = Script()
        action.search(query=param.get("查询条件"))

    # AI模型管理
    elif func == "AddAiModel":
        action = AiModel()
        action.add(application_mode=param.get("应用模式"), algorithm=param.get("算法名称"), model_name=param.get("模型名称"),
                   model_desc=param.get("模型描述"), train_scale=param.get("训练比例"), test_scale=param.get("测试比例"),
                   timeout=param.get("超时时间"), file_name=param.get("模型数据"), params=param.get("参数设置"),
                   columns=param.get("列设置"))

    elif func == "UpdateAiModel":
        action = AiModel()
        update_map = param.get("修改内容")
        action.update(model=param.get("模型名称"), model_name=update_map.get("模型名称"), model_desc=update_map.get("模型描述"),
                      train_scale=update_map.get("训练比例"), test_scale=update_map.get("测试比例"),
                      timeout=update_map.get("超时时间"), file_name=update_map.get("模型数据"), params=update_map.get("参数设置"),
                      columns=update_map.get("列设置"))

    elif func == "TrainAiModel":
        action = AiModel()
        action.train_model(model_name=param.get("模型名称"))

    elif func == "TestAiModel":
        action = AiModel()
        action.test_model(model_name=param.get("模型名称"))

    elif func == "DeleteAiModel":
        action = AiModel()
        action.delete(model_name=param.get("模型名称"))

    elif func == "ImportDisturb":
        action = AiModel()
        action.import_disturb(model_name=param.get("模型名称"), file_name=param.get("文件名"))

    elif func == "AiModelDataClear":
        action = AiModel()
        action.data_clear(model_name=param.get("模型名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListAiModel":
        action = AiModel()
        action.search(query=param.get("查询条件"))

    # 邮箱管理
    elif func == "AddMail":
        action = Mail()
        action.add(mail_addr=param.get("邮箱地址"), mail_type=param.get("邮箱类型"), data_type=param.get("数据类型"),
                   send_protocol=param.get("发送协议类型"), send_server=param.get("发送服务器地址"), send_port=param.get("发送端口"),
                   receive_protocol=param.get("接收协议类型"), receive_server=param.get("接收服务器地址"),
                   receive_port=param.get("接收端口"), username=param.get("账号"), pwd=param.get("密码或授权码"),
                   proxy_name=param.get("代理名称"), platf_account=param.get("平台账号"))

    elif func == "UpdateMail":
        action = Mail()
        update_map = param.get("修改内容")
        action.update(mail=param.get("邮箱地址"), mail_addr=update_map.get("邮箱地址"), mail_type=update_map.get("邮箱类型"),
                      data_type=update_map.get("数据类型"), send_protocol=update_map.get("发送协议类型"),
                      send_server=update_map.get("发送服务器地址"), send_port=update_map.get("发送端口"),
                      receive_protocol=update_map.get("接收协议类型"), receive_server=update_map.get("接收服务器地址"),
                      receive_port=update_map.get("接收端口"), username=update_map.get("账号"), pwd=update_map.get("密码或授权码"),
                      proxy_name=update_map.get("代理名称"), platf_account=update_map.get("平台账号"))

    elif func == "TestMail":
        action = Mail()
        action.test(mail_addr=param.get("邮箱地址"))

    elif func == "DeleteMail":
        action = Mail()
        action.delete(mail_addr=param.get("邮箱地址"))

    elif func == "MailDataClear":
        action = Mail()
        action.data_clear(mail_addr=param.get("邮箱地址"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListMail":
        action = Mail()
        action.search(query=param.get("查询条件"))

    # FTP管理
    elif func == "AddFTP":
        action = FTP()
        action.add(server_name=param.get("服务器名称"), ip=param.get("服务器IP"), port=param.get("服务器端口"),
                   username=param.get("用户名"), pwd=param.get("密码"), server_type=param.get("服务器类型"),
                   encoding=param.get("服务器编码"), data_type=param.get("数据类型"))

    elif func == "UpdateFTP":
        action = FTP()
        update_map = param.get("修改内容")
        action.update(ftp=param.get("服务器名称"), server_name=update_map.get("服务器名称"), ip=update_map.get("服务器IP"),
                      port=update_map.get("服务器端口"), username=update_map.get("用户名"), pwd=update_map.get("密码"),
                      server_type=update_map.get("服务器类型"), encoding=update_map.get("服务器编码"),
                      data_type=update_map.get("数据类型"))

    elif func == "TestFTP":
        action = FTP()
        action.test(server_name=param.get("服务器名称"))

    elif func == "DeleteFTP":
        action = FTP()
        action.delete(server_name=param.get("服务器名称"))

    elif func == "FTPDataClear":
        action = FTP()
        action.data_clear(server_name=param.get("服务器名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListFTP":
        action = FTP()
        action.search(query=param.get("查询条件"))

    # 第三方系统管理
    elif func == "AddThirdSystem":
        action = ThirdSystem()
        action.add(platform=param.get("平台名称"), visit_url=param.get("平台地址"), network_tag=param.get("平台网络标识"),
                   browser_type=param.get("浏览器类型"), browser_timeout=param.get("浏览器超时时间"),
                   session_timeout=param.get("空闲刷新时间"), data_type=param.get("数据类型"),
                   first_click_set=param.get("是否优先点击页面元素"), enable_proxy_set=param.get("是否启用代理"),
                   enable_login_set=param.get("是否验证登录"))

    elif func == "TestThirdSystem":
        action = ThirdSystem()
        action.test(platform=param.get("平台名称"), code=param.get("手机验证码"))

    elif func == "UpdateThirdSystem":
        action = ThirdSystem()
        update_map = param.get("修改内容")
        action.update(system=param.get("平台名称"), platform=update_map.get("平台名称"), visit_url=update_map.get("平台地址"),
                      network_tag=update_map.get("平台网络标识"), browser_type=update_map.get("浏览器类型"),
                      browser_timeout=update_map.get("浏览器超时时间"), session_timeout=update_map.get("空闲刷新时间"),
                      data_type=update_map.get("数据类型"), first_click_set=update_map.get("是否优先点击页面元素"),
                      enable_proxy_set=update_map.get("是否启用代理"), enable_login_set=update_map.get("是否验证登录"))

    elif func == "DeleteThirdSystem":
        action = ThirdSystem()
        action.delete(platform=param.get("平台名称"))

    elif func == "ThirdSystemDataClear":
        action = ThirdSystem()
        action.data_clear(platform=param.get("平台名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListThirdSystem":
        action = ThirdSystem()
        action.search(query=param.get("查询条件"))

    # 第三方接口管理
    elif func == "AddInterface":
        action = Interface()
        action.add(interface_name=param.get("接口名称"), interface_type=param.get("接口类型"),
                   interface_url=param.get("接口url"), data_type=param.get("数据类型"),
                   interface_namespace=param.get("接口空间名"), interface_method=param.get("接口方法名"),
                   request_type=param.get("请求方式"), timeout=param.get("超时时间"), proxy_name=param.get("代理名称"),
                   result_sample=param.get("返回结果样例"), request_header=param.get("接口请求头"),
                   request_parameter=param.get("接口参数"), request_body=param.get("请求体内容"))

    elif func == "TestInterface":
        action = Interface()
        action.test(interface_name=param.get("接口名称"))

    elif func == "UpdateInterface":
        action = Interface()
        update_map = param.get("修改内容")
        action.update(interface=param.get("接口名称"), interface_name=update_map.get("接口名称"),
                      interface_type=update_map.get("接口类型"), interface_url=update_map.get("接口url"),
                      data_type=update_map.get("数据类型"), interface_namespace=update_map.get("接口空间名"),
                      interface_method=update_map.get("接口方法名"), request_type=update_map.get("请求方式"),
                      timeout=update_map.get("超时时间"), proxy_name=update_map.get("代理名称"),
                      result_sample=update_map.get("返回结果样例"), request_header=update_map.get("接口请求头"),
                      request_parameter=update_map.get("接口参数"), request_body=update_map.get("请求体内容"))

    elif func == "DeleteInterface":
        action = Interface()
        action.delete(interface_name=param.get("接口名称"))

    elif func == "InterfaceDataClear":
        action = Interface()
        action.data_clear(interface_name=param.get("接口名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "ListInterface":
        action = Interface()
        action.search(query=param.get("查询条件"))

    # 文件目录管理
    elif func == "MkDir":
        action = File(catalog=param.get("目录分类"))
        action.mkdir(parent_dir=param.get("目标目录"), dir_name=param.get("目录名"))

    elif func == "UpdateDir":
        action = File(catalog=param.get("目录分类"))
        action.update_dir(target_dir=param.get("目标目录"), new_dir=param.get("目录名"))

    elif func == "DeleteDir":
        action = File(catalog=param.get("目录分类"))
        action.delete_dir(dir_name=param.get("目标目录"))

    elif func == "UploadFile":
        action = File(catalog=param.get("目录分类"))
        action.upload_file(dir_name=param.get("目标目录"), catalog=param.get("文件类别"), file_name=param.get("文件名"))

    elif func == "DownloadFile":
        action = File(catalog=param.get("目录分类"))
        action.download_file(dir_name=param.get("目标目录"), file_name=param.get("文件名"))

    elif func == "DeleteFile":
        action = File(catalog=param.get("目录分类"))
        action.delete_file(dir_name=param.get("目标目录"), file_name=param.get("文件名"))

    elif func == "DownloadFileBatch":
        action = File(catalog=param.get("目录分类"))
        action.download_file_batch(dir_name=param.get("目标目录"), file_names=param.get("文件名"))

    elif func == "DeleteFileBatch":
        action = File(catalog=param.get("目录分类"))
        action.delete_file_batch(dir_name=param.get("目标目录"), file_names=param.get("文件名"))

    elif func == "DirDataClear":
        action = File(catalog=param.get("目录分类"))
        action.data_clear(obj=param.get("目标目录"))

    # 指令集
    elif func == "AddCmdSet":
        action = CmdSet()
        action.add(cmd_name=param.get("指令名称"), cmd_category=param.get("指令类别"), cmd_use=param.get("指令用途"),
                   level=param.get("网元分类"), vendor=param.get("厂家"), model=param.get("设备型号"),
                   login_type=param.get("登录模式"), public_cmd=param.get("公有指令"), sensitive_cmd=param.get("隐藏输入指令"),
                   personal_cmd=param.get("个性指令"), cmd_timeout=param.get("指令等待超时"), command=param.get("指令"),
                   remark=param.get("说明"), rulerx_analyzer=param.get("指令解析模版"), cmd_pagedown=param.get("指令翻页符"),
                   expected_return=param.get("期待返回的结束符"), sensitive_regex=param.get("隐藏指令返回"))

    elif func == "UpdateCmdSetStatus":
        action = CmdSet()
        action.update_status(query=param.get("查询条件"), status=param.get("状态"))

    elif func == "DeleteCmdSet":
        action = CmdSet()
        action.delete(query=param.get("查询条件"))

    elif func == "CmdSetInput":
        action = CmdSet()
        action.set_input_param(query=param.get("查询条件"), params=param.get("参数信息"))

    elif func == "CmdSetOutput":
        action = CmdSet()
        action.set_output_param(query=param.get("查询条件"), regex_param=param.get("正则参数"),
                                table_param=param.get("二维表参数"))

    elif func == "CmdSetWash":
        action = CmdSet()
        action.set_log_wash(query=param.get("查询条件"), wash_direction=param.get("日志清洗方向"),
                            wash_by_date=param.get("按日期清洗"), wash_by_key=param.get("按关键字清洗"))

    elif func == "CmdSetDataClear":
        action = CmdSet()
        action.data_clear(cmd_name=param.get("指令名称"), fuzzy_match=param.get("模糊匹配"))

    # 指令模版
    elif func == "AddCmdTpl":
        action = CmdTemplate()
        action.add(template_name=param.get("模版名称"), field=param.get("专业领域"), levels=param.get("网络层级"),
                   mode=param.get("选择方式"), remark=param.get("备注"))

    elif func == "UpdateCmdTpl":
        action = CmdTemplate()
        update_map = param.get("修改内容")
        action.update(template_name=param.get("模版名称"), basic_info=update_map.get("模版基本信息"),
                      auto_follow_strategy=update_map.get("自动跟进策略配置"), bind_ne=update_map.get("模版网元绑定"),
                      bind_ne_level=update_map.get("模版网元类型绑定"), bind_cmd=update_map.get("模版指令绑定"))

    elif func == "UpdateCmpTplStatus":
        action = CmdTemplate()
        action.updateStatus(template_name=param.get("模版名称"), status=param.get("状态"))

    elif func == "CmdTplDataClear":
        action = CmdTemplate()
        action.data_clear(template_name=param.get("模版名称"), fuzzy_match=param.get("模糊匹配"))

    # 通用解析模版配置
    elif func == "AddRulerX":
        action = RulerX()
        action.add(basic_cfg=param.get("基本信息配置"), result_format_cfg=param.get("结果格式化配置"),
                   segment_cfg=param.get("分段规则配置"), format_table_cfg=param.get("格式化二维表配置"),
                   judge_type=param.get("选择判断规则"), judge_cfg=param.get("判断规则配置"))

    elif func == "RulerXDataClear":
        action = RulerX()
        action.data_clear(analyzer_name=param.get("解析模版名称"), fuzzy_match=param.get("模糊匹配"))

    # 正则模版管理
    elif func == "AddRegexpTemp":
        action = RegexpTemplate()
        action.add(regexp_name=param.get("正则模版名称"), remark=param.get("模版描述"), regexp_info=param.get("正则魔方"))

    elif func == "RegexpDataClear":
        action = RegexpTemplate()
        action.data_clear(regexp_name=param.get("正则模版名称"), fuzzy_match=param.get("模糊匹配"))

    # 数据拼盘
    elif func == "AddEDataTpl":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.add_table(table_name=param.get("数据表名称"), field=param.get("专业领域"), remark=param.get("备注"),
                         cmd=param.get("取参指令"), regexp_start=param.get("段开始特征行"),
                         regexp_end=param.get("段结束特征行"), sample=param.get("样例数据"))

    elif func == "UpdateEDataTpl":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        update_map = param.get("修改内容")
        action.update_table(table=param.get("数据表名称"), table_name=update_map.get("数据表名称"),
                            field=update_map.get("专业领域"), remark=update_map.get("备注"),
                            cmd=update_map.get("取参指令"), regexp_start=update_map.get("段开始特征行"),
                            regexp_end=update_map.get("段结束特征行"), sample=update_map.get("样例数据"))

    elif func == "DeleteEDataTpl":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.delete_table(table_name=param.get("数据表名称"))

    elif func == "EDataSetCol":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.set_cols(table_name=param.get("数据表名称"), col_set=param.get("列配置"))

    elif func == "EDataSetSearchCol":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.set_search_col()

    elif func == "EDataSetFrozenCol":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.set_frozen_col()

    elif func == "EDataConfigUpdateRule":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.configure_update_rule(table_name=param.get("数据表名称"), cmd=param.get("取参指令"),
                                     rulerX=param.get("指令解析模版"), result_bind=param.get("二维表结果绑定"))

    elif func == "AddJoinEDataTpl":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.add_join_table(join_table_list=param.get("合并表名称"), join_type=param.get("关联方式"),
                              left_table_set=param.get("左表配置"), right_table_set=param.get("右表配置"),
                              new_table_name=param.get("数据表名称"), field=param.get("专业领域"),
                              new_table_set=param.get("新表配置"))

    elif func == "AddUnionEDataTpl":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.add_union_table(join_table_list=param.get("合并表名称"), join_type=param.get("关联方式"),
                               join_table_set=param.get("合并表配置"), new_table_name=param.get("数据表名称"),
                               field=param.get("专业领域"), new_table_set=param.get("新表配置"))

    elif func == "EDataBindNE":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.bind_netunit(table_name=param.get("数据表名称"), netunit_list=param.get("网元列表"))

    elif func == "EDataUpdateStatus":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.update_status(table_name=param.get("数据表名称"), set_status=param.get("状态"))

    elif func == "EDataDataClear":
        action = EDataTemplate(temp_type=param.get("模版类型"))
        action.data_clear(table_name=param.get("数据表名称"), fuzzy_match=param.get("模糊匹配"))

    # 我的监控
    elif func == "ClickDashboardButton":
        action = Monitor()
        action.clickButton(button_name=param.get("按钮"))

    elif func == "ShowDashboard":
        action = Monitor()
        action.showDashboard(dashboard_name=param.get("仪表盘名称"))

    elif func == "SetDefaultDashboard":
        action = Monitor()
        action.setDefaultDashboard(dashboard_info=param.get("仪表盘配置"))

    elif func == "SetMyDashboard":
        action = Monitor()
        action.setMyDashboard(dashboard_info=param.get("仪表盘配置"))

    elif func == "AddDashboard":
        action = Monitor()
        action.addDashboard(dashboard_info=param.get("仪表盘配置"))

    elif func == "EditDashboard":
        action = Monitor()
        update_map = param.get("修改内容")
        action.editDashboard(dashboard_name=param.get("仪表盘名称"), dashboard_info=update_map.get("仪表盘配置"))

    elif func == "DeleteDashboard":
        action = Monitor()
        action.deleteDashboard(dashboard_name=param.get("仪表盘名称"))

    elif func == "ClearDashboard":
        action = Monitor()
        action.clearDashboard(dashboard_name=param.get("仪表盘名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "AddImage":
        action = Monitor()
        action.addImage(image_info=param.get("图像配置"))

    elif func == "DeleteImage":
        action = Monitor()
        action.deleteImage(image_name=param.get("图像名称"))

    elif func == "ClearImage":
        action = Monitor()
        action.clearImage(image_name=param.get("图像名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "AddDictionary":
        action = Monitor()
        action.addDictionary(dictionary_info=param.get("字典配置"))

    elif func == "UpdateDictionary":
        action = Monitor()
        update_map = param.get("修改内容")
        action.editDictionary(dict_name=param.get("字典名"), dictionary_info=update_map.get("字典配置"))

    elif func == "DeleteDictionary":
        action = Monitor()
        action.deleteDictionary(dict_name=param.get("字典名"))

    elif func == "ClearDictionary":
        action = Monitor()
        action.clearDictionary(dict_name=param.get("字典名"), fuzzy_match=param.get("模糊匹配"))

    elif func == "FieldClassify":
        action = Monitor()
        action.fieldClassify(table_name=param.get("表中文名称"), x_list=param.get("维度字段"),
                             y_list=param.get("度量字段"), g_list=param.get("分组字段"))

    elif func == "FieldConversion":
        action = Monitor()
        action.fieldConversion(table_name=param.get("表中文名称"), conversion=param.get("转化配置"))

    elif func == "AddInImage":
        action = Monitor()
        action.addInImage(dashboard_name=param.get("仪表盘名称"), image_list=param.get("图像列表"))

    # 任务配置
    elif func == "AddTask":
        action = TaskManage()
        action.add(task_name=param.get("任务名称"), task_type=param.get("模版类型"), bind_task=param.get("绑定任务名称"),
                   time_turner=param.get("配置定时任务"), timing_conf=param.get("定时配置"), remark=param.get("任务说明"))

    elif func == "UpdateTask":
        action = TaskManage()
        update_map = param.get("修改内容")
        action.update(task=param.get("任务名称"), task_name=update_map.get("任务名称"), time_turner=update_map.get("配置定时任务"),
                      timing_conf=update_map.get("定时配置"), remark=update_map.get("任务说明"))

    elif func == "UpdateTaskStatus":
        action = TaskManage()
        action.updateStatus(task_name=param.get("任务名称"), status=param.get("状态"))

    elif func == "DeleteTask":
        action = TaskManage()
        action.delete(task_name=param.get("任务名称"))

    elif func == "TriggerTask":
        action = TaskManage()
        action.triggerTask(task_name=param.get("任务名称"))

    elif func == "TaskDataClear":
        action = TaskManage()
        action.data_clear(query=param.get("查询条件"), fuzzy_match=param.get("模糊匹配"))

    else:
        log.error("无效的动作函数")
        run_flag = False

    return run_flag


""" 
    {
        "操作": "CmdSetInput",
        "参数": {
            "查询条件": {
                "指令名称": "auto_指令_单参数",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": "ME60"
            },
            "参数信息": {
                "输出参数": ""
            }
        }
    }
    
    {
        "操作": "CmdSetOutput",
        "参数": {
            "查询条件": {
                "指令名称": "auto_指令_单参数",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": "ME60"
            },
            "正则参数": {
                "参数名称": "result_ping",
                "参数说明": "ping解析",
                "私有参数": "否",
                "正则魔方": {
                    "设置方式": "选择",
                    "正则模版名称": "auto_正则模版_获取丢包率"
                },
                "取值": "取匹配到第一个值"
            }
        }
    }

    {
        "操作": "CreateProcessTask",
        "参数": {
            "流程名称": "网元基础信息",
            "任务配置": {
                "任务名称": "auto_指令任务_date",
                "配置定时任务": "关闭"
            }
        }   
    }
    
    {
        "操作": "CreateProcessTask",
        "参数": {
            "流程名称": "网元基础信息",
            "任务配置": {
                "任务名称": "auto_指令任务_date",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                
                },
                "任务说明": "auto_指令任务_date"
            }
        }   
    }
    
    {
        "操作": "UpdateTask",
        "参数": {
            "任务名称": "auto_指令任务_date",
            "修改内容": {
                "任务名称": "auto_指令任务_date",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                
                },
                "任务说明": "auto_指令任务_date"
            }
        }   
    }  
    
    
    {
        "操作": "UpdateTaskStatus",
        "参数": {
            "任务名称": "auto_指令任务_date",
            "状态": "启用"
        }   
    }
        
    {
        "操作": "DeleteTask",
        "参数": {
            "任务名称": "auto_指令任务_date"
        }
    }
    
    {
        "操作": "TriggerTask",
        "参数": {
            "任务名称": "auto_指令任务_date"
        }
    }
    
    {
        "操作": "TriggerTask",
        "参数": {
            "任务名称": "auto_流程_pw0315"
        }
    }
    
    
    {
        "操作": "CopyProcess",
        "参数": {
            "流程名称": "auto_流程_pw0315",
            "主流程名称": "auto_流程_pw0315",
            "子流程名称列表": "auto_流程_pw0315"
        }
    }
"""