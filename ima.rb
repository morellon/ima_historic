require "net/http"

uri = URI('http://www.anbima.com.br/ima/IMA-geral-down.asp')
res = Net::HTTP.post_form(uri, 'saida' => 'csv', 'Idioma' => 'PT', 'Dt_ref' => "15082012")
raw_indexes = res.body.split(/\r?\n/)[2..-1]
indexes = {}
raw_indexes.each do |idx|
  idx_parts = idx.split(';')
  key = idx_parts[0..1].join(" ")
  indexes[key] = idx_parts[3].sub(".", "").sub(",", ".").to_f
end
