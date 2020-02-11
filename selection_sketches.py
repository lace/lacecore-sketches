lace.sel(mesh).keep_vertices()

lace.sel(mesh).mutate().keep_vertices()
lace.sel(mesh).m().keep_vertices()
lace.mutate.sel(mesh).keep_vertices()
lace.mut.sel(mesh).keep_vertices()
lace.mut.sel(mesh).keep_vertices()

lace.sel(mesh).mut_keep_vertices()
lace.sel(mesh).mut_keep_vertices()


lace.sel(mesh).keep_vertices()
lace.sel(mesh).copy().keep_vertices()

lace.chain(lace.sel.keep_vertices())

lace.sel(mesh).keep

with lace.sel(mesh) as sel:
  lace.sel.keep_vertices(verts)(mesh)

with lace.sel(mesh) as sel:
  sel.keep_vertices(verts)
  sel.flip_faces()

# Create shallow copy:
head_mesh = lace.sel(mesh).keep_segments('head')

head_pc = lace.chain(mesh)(
  lace.sel.keep_segments('head'),
  lace.sel.drop_all_faces()
)

# In place:
lace.sel(mutate=mesh).keep_segments('head')

mesh.chain_select(mutable=True)
  .keep_vertices()
  .cut_across_axis()
  .end()

mesh.sel(mutable=True)
  .keep_vertices()
  .cut_across_axis()
  .end()

new_mesh = mesh.selection(mutable=True)
  .keep_groups(["a", "b", "c"])
  .keep_vertices()
  .cut_across_axis()
  .end()

mesh
  .keep_vertices()
  .cut_across_axis()
