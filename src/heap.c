#include "dukpy.h"


DukHeap *DukHeap_new(void)
{
    DukHeap *self;

    self = PyObject_New(DukHeap, &DukHeap_Type);
    if (self == NULL)
        return NULL;

    self->ctx = duk_create_heap_default();

    printf("DukHeap_new (self=%p, self->ctx=%p)\n", self, self->ctx);

    /* heap_stash.heap = (void *)self */
    duk_push_heap_stash(self->ctx);
    duk_push_pointer(self->ctx, self);
    duk_put_prop_string(self->ctx, -2, "heap");
    duk_pop(self->ctx);

    printf("end of DukHeap_new\n");
    return self;
}

DukHeap *DukHeap_from_ctx(duk_context *ctx)
{
    DukHeap *self;

    duk_push_heap_stash(ctx);
    duk_get_prop_string(ctx, -1, "heap");
    self = duk_get_pointer(ctx, -1);
    assert(self);
    duk_pop_n(ctx, 2);

    return self;
}

void DukHeap_incref_from_ctx(duk_context *ctx)
{
    Py_INCREF(DukHeap_from_ctx(ctx));
}

int DukHeap_decref_from_ctx(duk_context *ctx)
{
    DukHeap *heap;
    Py_ssize_t refcount;

    heap = DukHeap_from_ctx(ctx);
    refcount = heap->ob_base.ob_refcnt;
    Py_DECREF(heap);

    return refcount == 1;
}

static void DukHeap_dealloc(DukHeap *self)
{
    printf("DukHeap_dealloc (self=%p, self->ctx=%p)\n", self, self->ctx);
    //duk_destroy_heap(self->ctx);
    Py_TYPE(self)->tp_free((PyObject *)self);
    printf("end of DukHeap_dealloc\n");
}

PyTypeObject DukHeap_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "Heap",                          /* tp_name */
    sizeof(DukHeap),                 /* tp_basicsize */
    0,                               /* tp_itemsize */
    (destructor)DukHeap_dealloc,     /* tp_dealloc */
    0,                               /* tp_print */
    0,                               /* tp_getattr */
    0,                               /* tp_setattr */
    0,                               /* tp_reserved */
    0,                               /* tp_repr */
    0,                               /* tp_as_number */
    0,                               /* tp_as_sequence */
    0,                               /* tp_as_mapping */
    0,                               /* tp_hash  */
    0,                               /* tp_call */
    0,                               /* tp_str */
    0,                               /* tp_getattro */
    0,                               /* tp_setattro */
    0,                               /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,              /* tp_flags */
    "Duktape heap",                  /* tp_doc */
};
