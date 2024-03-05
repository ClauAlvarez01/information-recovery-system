export interface Document{
    doc_id: string,
    title: string,
    text: string,
    author: string,
    bib: string
}

export interface Metrics{
    precision: Metric
    recovered: Metric
    f1: Metric
    fallout: Metric
}

export interface Metric{
    boolean: string,
    lsi: string
}

export interface Query{
    query_id: string,
    text: string
}