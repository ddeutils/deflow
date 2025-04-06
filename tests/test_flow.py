from ddeutil.workflow import config, make_registry

from deflow.flow import Flow


def test_flow_stream():
    print(config.conf_path)

    stream_flow = Flow("s_first_d")
    print(stream_flow)


def test_flow_stream_run():
    print(config.regis_call)

    registries = make_registry("tasks")
    print(registries)

    stream_flow = Flow("s_first_d")
    rs = stream_flow.run(mode="N")
    print(rs.context)
    # assert rs.context == {
    #     'params': {'stream': 's_first_d', 'run-mode': 'N'},
    #     'release': {
    #         'type': 'manual',
    #         'logical_date': datetime(2025, 4, 6, 14, 45, 15, 843961),
    #         'release': '2025-04-06 14:45:15'
    #     },
    #     'outputs': {
    #         'jobs': {
    #             'start-steam': {
    #                 'stages': {
    #                     'get-stream': {'outputs': {'name': 's_first_d'}},
    #                     'start-stream': {'outputs': {'audit-date': datetime(2025, 4, 1, 1, 0)}},
    #                     'priority-group': {'outputs': {'items': [1, 2]}},
    #                     'start-priority-group': {
    #                         'outputs': {
    #                             'items': [1, 2],
    #                             'foreach': {
    #                                 1: {'stages': {}},
    #                                 2: {'stages': {}},
    #                             },
    #                         },
    #                     },
    #                 },
    #             },
    #         },
    #     },
    # }
