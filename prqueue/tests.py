# coding: utf-8
from developers.models import Product, ProductQueue, Developer


test_qe = ProductQueue.objects.get(pk=1)

print test_qe

all_dev_in_test_q = test_qe.all_developers()

developers = Developer.objects.filter(id__in=all_dev_in_test_q)

for dev in developers:
    print u'======do it for name %s ======' % dev
    for dev_q in test_qe.dev_queue.all():
        print u'****process developers queue named %s********' % dev_q
        _curr_dev = dev_q.current()
        print u'=== current dev is %s ===' % _curr_dev
        print dev == _curr_dev